from _decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

from .forms import LotForm, LotCommentForm
from .models import Lot, LotComment, LotSection
from django.views import View


def main(request):
    lots = Lot.objects.all().order_by('-rating', '-highest_price')[:3]

    return render(request, 'index.html', {'popular_lots': lots})


class LotCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):

    permission_required = 'lot.add_lot'

    def get(self, request):
        lot_form = LotForm(initial={'title': 'Название по умолчанию'})

        return render(request, 'create_lot.html', {
            'lot_form': lot_form
        })

    def post(self, request):
        lot_form = LotForm(request.POST, request.FILES)

        if lot_form.is_valid():
            # Lot.objects.create(user=request.user, **lot_form.cleaned_data)
            lot = lot_form.save()
            lot.user = request.user
            lot.highest_price = lot.starting_price
            lot.save()

            return redirect('/lots/')
        return render(request, 'create_lot.html', {'lot_form': lot_form})


def lots_view(request):
    if request.method == 'GET':
        if request.GET.getlist('section'):
            lots_list = Lot.objects.filter(section__in=request.GET.getlist('section')).order_by('-rating',
                                                                                                '-highest_price')
        else:
            lots_list = Lot.objects.all().order_by('-rating', '-highest_price')

        paginator = Paginator(lots_list, 1)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)

        try:
            page_lots = paginator.page(page_num)
        except PageNotAnInteger:
            page_lots = paginator.page(1)
        except EmptyPage:
            page_lots = paginator.page(paginator.num_pages)

        return render(request, 'lots.html', {
            'page_obj': page_obj,
            'page_lots': page_lots,
            'sections': LotSection.objects.all(),
        })


@login_required()
def specific_lot_view(request, pk):
    lot = Lot.objects.get(pk=pk)
    comments = lot.lotcomment_set.all().order_by('-date_time')
    comment_form = LotCommentForm()

    min_price = int(lot.highest_price) + 1
    max_price = int(request.user.profile.balance)

    context = dict(lot=lot, comments=comments, comment_form=comment_form, min_price=min_price, max_price=max_price)

    if request.user.is_authenticated:
        favorites = request.user.favorites.all()
        context['favorites'] = favorites
    return render(request, 'lots_detail_view.html', context)


# создание комментария
@login_required()
def create_lot_comment(request, pk):
    comment_form = LotCommentForm(request.POST)
    current_lot = Lot.objects.get(pk=pk)

    if comment_form.is_valid():
        LotComment.objects.create(user=request.user, lot_binding=current_lot, **comment_form.cleaned_data)

    return redirect('lot_page', pk=pk)


class LotEditView(LoginRequiredMixin, View):
    def get(self, request, lot_id):
        lot = Lot.objects.get(pk=lot_id)

        if lot.user != request.user:
            raise PermissionDenied()

        lot_form = LotForm(instance=lot)

        return render(request, 'edit_lot.html', {
            'lot_form': lot_form,
            'lot_id': lot_id,
        })

    def post(self, request, lot_id):
        lot = Lot.objects.get(pk=lot_id)
        # lot_form = LotForm(request.POST, request.FILES, instance=lot)
        lot_form = LotForm(request.POST, request.FILES)

        if lot_form.is_valid():
            lot_form.save()

        return redirect('lot_page', pk=lot_id)


@login_required()
def add_to_favorites(request, lot_id):
    if request.method == 'GET':
        lot = Lot.objects.get(pk=lot_id)

        if request.user == lot.user:
            return HttpResponseForbidden()

        if lot in request.user.favorites.all():
            return redirect('lot_page', lot_id)

        request.user.favorites.add(lot)

        lot.rating += 1
        lot.save(update_fields=['rating'])

        return redirect('lot_page', lot_id)


@login_required()
def remove_from_favorites(request, lot_id):
    if request.method == 'GET':
        lot = Lot.objects.get(pk=lot_id)

        if lot not in request.user.favorites.all():
            redirect('lot_page', lot_id)

        request.user.favorites.remove(lot)

        lot.rating -= 1
        lot.save(update_fields=['rating'])

        return redirect('lot_page', lot_id)


@login_required()
def raise_price(request, lot_id):
    if request.method == 'GET':
        return redirect('lot_page', lot_id)

    if request.method == 'POST':
        # переписать валидацию в самой форме (на стороне клиента)
        lot = Lot.objects.get(pk=lot_id)

        if lot.is_sold:
            return redirect('lot_page', lot_id)

        if request.user == lot.user:
            return HttpResponseForbidden()

        new_price = Decimal(request.POST.get('new_price'))

        if new_price <= lot.highest_price:
            # return render(request, 'lots_detail_view.html', lot_id)

            return redirect('lot_page', lot_id)

        lot.highest_price = new_price
        lot.current_buyer = request.user
        lot.save(update_fields=['highest_price', 'current_buyer'])

        return redirect('lot_page', lot_id)

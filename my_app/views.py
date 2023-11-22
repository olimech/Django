from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(f'Главная страница')


def me(request, full_name, age, hobby):
    return HttpResponse(f'Меня зовут, {full_name}, мне {age} лет и я пишу программу на {hobby}')


def about(request, sity):
    return HttpResponse(f'Я приехал из города ,{sity} в школе отличная успеваемость, люблю учиться')


def my_contact(request, contact, telegram):
    return HttpResponse(f'Мои контакты: Ссылка на GitHub: {contact} Связь с телеграммом: {telegram}')
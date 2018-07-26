from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from quran.utils import *
import json


@csrf_exempt
def main_view(request, purchased="", usage_count=1):
    print("main")
    payload = json.loads(request.POST['payload'])
    if payload.get('state'):
        if payload['state'] != 'FAILED':
            purchased = 'purchased'
    print(purchased)
    surahs = get_surahs_list_with_index()
    return render(request, "main.xml", context={'surahs': surahs, 'purchased': purchased,
                                                'usage_count': usage_count + 1})


@csrf_exempt
def surah_view(request, purchased="", usage_count=1):
    print("surah")
    payload = json.loads(request.POST['payload'])
    if payload.get('purchases'):
        if len(payload['purchases']) > 0:
            purchased = 'purchased'
    surah_number = payload.get('surah_number')
    surah_name = get_surah_name(surah_number)
    readers_list = get_readers_list()
    translators_list = get_translators_list()
    surah_verses_count_list = get_surah_verses_count_list(surah_number)
    return render(request, "surah.xml", context={'surah_name': surah_name, 'readers': readers_list,
                                                 'translators': translators_list, 'surah_number': surah_number,
                                                 'surah_verses_count_list': surah_verses_count_list,
                                                 'purchased': purchased,
                                                 'usage_count': usage_count + 1})


@csrf_exempt
def verse_view(request, surah_number, verse_number=-1, translator_id="", reader_id="", purchased="", usage_count=1):
    print("verse")
    payload = json.loads(request.POST['payload'])
    if verse_number == -1:
        verse_number = payload.get('verse_number')
    if translator_id == "":
        translator_id = payload.get('translator_id')
    if reader_id == "":
        reader_id = payload.get('reader_id')
    surah_name = get_surah_name(surah_number)
    verse_audio_url = get_verse_audio_url(surah_number, verse_number, reader_id)
    verse_image_url = get_verse_image_url(surah_number, verse_number)
    verse_translation_text = get_verse_translation_text(surah_number, verse_number, translator_id)
    next_verse_button_url = get_next_verse_button_url(surah_number, verse_number, translator_id, reader_id)
    prev_verse_button_url = get_prev_verse_button_url(surah_number, verse_number, translator_id, reader_id)
    return render(request, "verse.xml", context={"surah_name": surah_name,
                                                 "verse_number": get_persian_number(verse_number),
                                                 "verse_audio_url": verse_audio_url,
                                                 "verse_image_url": verse_image_url,
                                                 "verse_translation_text": verse_translation_text,
                                                 "next_verse_button_url": next_verse_button_url,
                                                 "prev_verse_button_url": prev_verse_button_url,
                                                 "purchased": purchased,
                                                 'usage_count': usage_count + 1})


@csrf_exempt
def buy_view(request, usage_count=1):
    return render(request, "buy.xml", context={'usage_count': usage_count + 1})

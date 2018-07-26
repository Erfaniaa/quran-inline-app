import requests

API_URL = "http://api.alquran.cloud/"
CDN_URL = "http://cdn.alquran.cloud/media/"

READERS = [("ar.abdulbasitmurattal", "عبدالباسط"), ("ar.abdullahbasfar", "عبدالله بصفر"),
           ("ar.abdurrahmaansudais", "عبدالرحمن السديس"), ("ar.abdulsamad", "عبدالصمد"),
           ("ar.shaatree", "ابوبکر الشاطری"), ("ar.ahmedajamy", "احمد بن علی العجمی"), ("ar.alafasy", "العفاسی"),
           ("ar.hanirifai", "هانی رفاعی"), ("ar.husary", "حصری"), ("ar.husarymujawwad", "حصری تحقیق"),
           ("ar.hudhaify", "حذیفی"), ("ar.ibrahimakhbar", "ابراهیم اخدر"), ("ar.mahermuaiqly", "ماهر المعیقلی"),
           ("ar.minshawi", "منشاوی"), ("ar.minshawimujawwad", "منشاوی تحقیق"), ("ar.muhammadayyoub", "محمد ایوب"),
           ("ar.muhammadjibreel", "محمد جبریل"), ("ar.saoodshuraym", "سعود بن ابراهیم الشریم"),
           ("en.walk", "ابراهیم واک"), ("fa.hedayatfarfooladvand", "فولادوند - هدایت‌فر"), ("ar.parhizgar", "پرهیزگار"),
           ("ur.khan", "شمشاد علی خان"), ("zh.chinese", "قاری چینی"), ("fr.leclerc", "یوسف لکرلک")]

TRANSLATORS = [("fa.ayati", "آیتی"), ("fa.fooladvand", "فولادوند"), ("fa.ghomshei", "الهی قمشه‌ای"),
               ("fa.makarem", "مکارم شیرازی"), ("fa.ansarian", "انصاریان"), ("fa.bahrampour", "بهرام‌پور"),
               ("fa.khorramshahi", "خرم‌شاهی"), ("fa.mojtabavi", "مجتبوی"), ("fa.khorramdel", "خرم‌دل"),
               ("fa.moezzi", "معزی"), ("fa.hedayatfarfooladvand", "فولادوند - هدایت‌فر")]

SURAHS = ["فاتحه", "بقرة", "آل عمران", "نساء", "مائده", "انعام", "اعراف", "انفال", "توبه", "يونس", "هود", "يوسف", "رعد",
          "ابراهيم", "حِجر", "نحل", "اسراء", "کهف", "مريم", "طه", "انبياء", "حج", "مؤمنون", "نور", "فرقان", "شعراء",
          "نمل", "قصص", "عنکبوت", "روم", "لقمان", "سجده", "احزاب", "سباء", "فاطر", "يس", "صافات", "ص", "زُمر", "غافر",
          "فصلت", "شوري", "زخرف", "دخان", "جاثيه", "احقاف", "محمّد", "فتح", "حُجُرات", "ق", "ذاريات", "طور", "نجم", "قمر",
          "رحمن", "واقعه", "حديد", "مجادله", "حشر", "ممتحنه", "صف", "جمعه", "منافقون", "تغابن", "طلاق", "تحريم", "ملک",
          "قلم", "الحاقه", "معارج", "نوح", "جن", "مُزمّل", "مُدثّر", "قيامت", "انسان", "مرسلات", "نبأ", "نازعات", "عبس",
          "تکوير", "انفطار", "مطففين", "انشقاق", "بروج", "طارق", "اعلي", "غاشيه", "فجر", "بلد", "شمس", "ليل", "ضحي",
          "انشراح", "تين", "علق", "قدر", "بينه", "زلزله", "عاديات", "قارعه", "تکاثر", "عصر", "همزه", "فيل", "قريش",
          "ماعون", "کوثر", "کافرون", "نصر", "مسد", "توحيد", "فلق", "ناس"]

SURAHS_WITH_NUMBER = ["۱. فاتحه", "۲. بقرة", "۳. آل عمران", "۴. نساء", "۵. مائده", "۶. انعام", "۷. اعراف", "۸. انفال",
                      "۹. توبه", "۱۰. يونس", "۱۱. هود", "۱۲. يوسف", "۱۳. رعد", "۱۴. ابراهيم", "۱۵. حِجر", "۱۶. نحل",
                      "۱۷. اسراء", "۱۸. کهف", "۱۹. مريم", "۲۰. طه", "۲۱. انبياء", "۲۲. حج", "۲۳. مؤمنون", "۲۴. نور",
                      "۲۵. فرقان", "۲۶. شعراء", "۲۷. نمل", "۲۸. قصص", "۲۹. عنکبوت", "۳۰. روم", "۳۱. لقمان", "۳۲. سجده",
                      "۳۳. احزاب", "۳۴. سباء", "۳۵. فاطر", "۳۶. يس", "۳۷. صافات", "۳۸. ص", "۳۹. زُمر", "۴۰. غافر",
                      "۴۱. فصلت", "۴۲. شوري", "۴۳. زخرف", "۴۴. دخان", "۴۵. جاثيه", "۴۶. احقاف", "۴۷. محمّد", "۴۸. فتح",
                      "۴۹. حُجُرات", "۵۰. ق", "۵۱. ذاريات", "۵۲. طور", "۵۳. نجم", "۵۴. قمر", "۵۵. رحمن", "۵۶. واقعه",
                      "۵۷. حديد", "۵۸. مجادله", "۵۹. حشر", "۶۰. ممتحنه", "۶۱. صف", "۶۲. جمعه", "۶۳. منافقون",
                      "۶۴. تغابن", "۶۵. طلاق", "۶۶. تحريم", "۶۷. ملک", "۶۸. قلم", "۶۹. الحاقه", "۷۰. معارج",
                      "۷۱. نوح", "۷۲. جن", "۷۳. مُزمّل", "۷۴. مُدثّر", "۷۵. قيامت", "۷۶. انسان", "۷۷. مرسلات", "۷۸. نبأ",
                      "۷۹. نازعات", "۸۰. عبس", "۸۱. تکوير", "۸۲. انفطار", "۸۳. مطففين", "۸۴. انشقاق", "۸۵. بروج",
                      "۸۶. طارق", "۸۷. اعلي", "۸۸. غاشيه", "۸۹. فجر", "۹۰. بلد", "۹۱. شمس", "۹۲. ليل", "۹۳. ضحي",
                      "۹۴. انشراح", "۹۵. تين", "۹۶. علق", "۹۷. قدر", "۹۸. بينه", "۹۹. زلزله", "۱۰۰. عاديات",
                      "۱۰۱. قارعه", "۱۰۲. تکاثر", "۱۰۳. عصر", "۱۰۴. همزه", "۱۰۵. فيل", "۱۰۶. قريش", "۱۰۷. ماعون",
                      "۱۰۸. کوثر", "۱۰۹. کافرون", "۱۱۰. نصر", "۱۱۱. مسد", "۱۱۲. توحيد", "۱۱۳. فلق", "۱۱۴. ناس"]

SURAH_VERSES_COUNT = [7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111, 110, 98, 135, 112,
                      78, 118, 64, 77, 227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88, 75, 85, 54, 53, 89, 59, 37,
                      35, 38, 29, 18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24, 13, 14, 11, 11, 18, 12, 12, 30, 52, 52,
                      44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42, 29, 19, 36, 25, 22, 17, 19, 26, 30, 20, 15, 21, 11, 8,
                      8, 19, 5, 8, 8, 11, 11, 8, 3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6]

PERSIAN_NUMBERS = '۰۱۲۳۴۵۶۷۸۹'
ENGLISH_NUMBERS = '0123456789'


def get_verse_image_url(surah_number, verse_number):
    url = CDN_URL + "image/" + str(surah_number) + "/" + str(verse_number)
    return url


def get_verse_audio_url(surah_number, verse_number, reader_id, quality="high"):
    surah_number = int(surah_number)
    verse_number = int(verse_number)
    verse_idx = sum(SURAH_VERSES_COUNT[0:max(surah_number - 1, 0)]) + verse_number
    url = CDN_URL + "audio/ayah/" + reader_id + "/" + str(verse_idx) + "/" + quality
    return url


def get_reader_id(reader_name):
    for reader in READERS:
        if reader[1] == reader_name:
            return reader[0]
    return ""


def get_reader_name(reader_id):
    for reader in READERS:
        if reader[0] == reader_id:
            return reader[1]
    return ""


def get_translator_name(translator_id):
    for translator in TRANSLATORS:
        if translator[0] == translator_id:
            return translator[1]
    return ""


def get_translator_id(translator_name):
    for translator in TRANSLATORS:
        if translator[1] == translator_name:
            return translator[0]
    return ""


def get_translator_ids():
    return [translator[0] for translator in TRANSLATORS]


def get_translator_names():
    return [translator[1] for translator in TRANSLATORS]


def get_reader_ids():
    return [reader[0] for reader in READERS]


def get_reader_names():
    return [reader[1] for reader in READERS]


def get_surah_name(surah_number):
    return SURAHS[int(surah_number) - 1]


def get_surahs_list_with_index():
    return [(i + 1, SURAHS_WITH_NUMBER[i]) for i in range(len(SURAHS_WITH_NUMBER))]


def get_readers_list():
    return READERS


def get_translators_list():
    return TRANSLATORS


def get_surah_verses_count(surah_number):
    return SURAH_VERSES_COUNT[int(surah_number) - 1]


def get_surah_verses_count_list(surah_number):
    count = SURAH_VERSES_COUNT[int(surah_number) - 1]
    return [(i + 1, get_persian_number(i + 1)) for i in range(count)]


def get_surah_number(surah_name):
    for idx, val in SURAHS:
        if val == surah_name:
            return idx + 1
    for idx, val in SURAHS_WITH_NUMBER:
        if val == surah_name:
            return idx + 1
    return -1


def get_persian_number(english_number):
    s = str(english_number)
    ret = ""
    for i in range(len(s)):
        ret = ret + PERSIAN_NUMBERS[int(s[i])]
    return ret


def get_verse_translation_text(surah_number, ayah_number, translator_id):
    url = API_URL + "ayah/" + str(surah_number) + ":" + str(ayah_number) + "/" + translator_id
    r = requests.get(url)
    verse_text = r.json()["data"]["text"]
    return verse_text


def get_next_verse_button_url(surah_number, verse_number, translator_id, reader_id):
    next_verse_number = int(verse_number)
    next_surah_number = int(surah_number)
    surah_verses_count = get_surah_verses_count(surah_number)
    if int(verse_number) == surah_verses_count:
        if int(surah_number) != len(SURAHS):
            next_verse_number = 1
            next_surah_number = next_surah_number + 1
    else:
        next_verse_number = next_verse_number + 1
    return "surah/" + str(next_surah_number) + "/" + str(next_verse_number) + "/" + \
           translator_id + "/" + reader_id + "/"


def get_prev_verse_button_url(surah_number, verse_number, translator_id, reader_id):
    prev_verse_number = int(verse_number)
    prev_surah_number = int(surah_number)
    prev_surah_verses_count = get_surah_verses_count(max(surah_number - 1, 1))
    if int(verse_number) == 1:
        if int(surah_number) != 1:
            prev_verse_number = prev_surah_verses_count
            prev_surah_number = prev_surah_number - 1
    else:
        prev_verse_number = prev_verse_number - 1
    return "surah/" + str(prev_surah_number) + "/" + str(prev_verse_number) + "/" + \
           translator_id + "/" + reader_id + "/"


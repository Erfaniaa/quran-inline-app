import requests
import json

API_URL = "http://alquran.cloud/"
CDN_URL = "http://cdn.alquran.cloud/media/"

READERS = [("ar.abdulbasitmurattal","عبدالباسط"), ("ar.abdullahbasfar","عبدالله بصفر"),
           ("ar.abdurrahmaansudais","عبدالرحمن السديس"), ("ar.abdulsamad","عبدالصمد"), ("ar.shaatree","ابوبکر الشاطری"),
           ("ar.ahmedajamy","احمد بن علی العجمی"), ("ar.alafasy","العفاسی"), ("ar.hanirifai","هانی رفاعی"),
           ("ar.husary","حصری"), ("ar.husarymujawwad","حصری تحقیق"), ("ar.hudhaify","حذیفی"),
           ("ar.ibrahimakhbar","ابراهیم اخدر"), ("ar.mahermuaiqly","ماهر المعیقلی"), ("ar.minshawi","منشاوی"),
           ("ar.minshawimujawwad","منشاوی تحقیق"), ("ar.muhammadayyoub","محمد ایوب"),
           ("ar.muhammadjibreel","محمد جبریل"), ("ar.saoodshuraym","سعود بن ابراهیم الشریم"), ("en.walk","ابراهیم واک"),
           ("fa.hedayatfarfooladvand","فولادوند - هدایت‌فر"), ("ar.parhizgar","پرهیزگار"), ("ur.khan","شمشاد علی خان"),
           ("zh.chinese","قاری چینی"), ("fr.leclerc","یوسف لکرلک")]

TRANSLATORS = [("fa.ayati","آیتی"), ("fa.fooladvand","فولادوند"), ("fa.ghomshei","الهی قمشه‌ای"),
               ("fa.makarem","مکارم شیرازی"), ("fa.ansarian","انصاریان"), ("fa.bahrampour","بهرام‌پور"),
               ("fa.khorramshahi","خرم‌شاهی"), ("fa.mojtabavi","مجتبوی"), ("fa.khorramdel","خرم‌دل"),
               ("fa.moezzi","معزی"), ("fa.hedayatfarfooladvand","فولادوند - هدایت‌فر")]

SURAHS = ["۱. فاتحه", "۲. بقرة", "۳. آل عمران", "۴. نساء", "۵. مائده", "۶. انعام", "۷. اعراف", "۸. انفال", "۹. توبه",
          "۱۰. يونس", "۱۱. هود", "۱۲. يوسف", "۱۳. رعد", "۱۴. ابراهيم", "۱۵. حِجر", "۱۶. نحل", "۱۷. اسراء", "۱۸. کهف",
          "۱۹. مريم", "۲۰. طه", "۲۱. انبياء", "۲۲. حج", "۲۳. مؤمنون", "۲۴. نور", "۲۵. فرقان", "۲۶. شعراء", "۲۷. نمل",
          "۲۸. قصص", "۲۹. عنکبوت", "۳۰. روم", "۳۱. لقمان", "۳۲. سجده", "۳۳. احزاب", "۳۴. سباء", "۳۵. فاطر", "۳۶. يس",
          "۳۷. صافات", "۳۸. ص", "۳۹. زُمر", "۴۰. غافر", "۴۱. فصلت", "۴۲. شوري", "۴۳. زخرف", "۴۴. دخان", "۴۵. جاثيه",
          "۴۶. احقاف", "۴۷. محمّد", "۴۸. فتح", "۴۹. حُجُرات", "۵۰. ق", "۵۱. ذاريات", "۵۲. طور", "۵۳. نجم", "۵۴. قمر",
          "۵۵. رحمن", "۵۶. واقعه", "۵۷. حديد", "۵۸. مجادله", "۵۹. حشر", "۶۰. ممتحنه", "۶۱. صف", "۶۲. جمعه",
          "۶۳. منافقون", "۶۴. تغابن", "۶۵. طلاق", "۶۶. تحريم", "۶۷. ملک", "۶۸. قلم", "۶۹. الحاقه", "۷۰. معارج",
          "۷۱. نوح", "۷۲. جن", "۷۳. مُزمّل", "۷۴. مُدثّر", "۷۵. قيامت", "۷۶. انسان", "۷۷. مرسلات", "۷۸. نبأ", "۷۹. نازعات",
          "۸۰. عبس", "۸۱. تکوير", "۸۲. انفطار", "۸۳. مطففين", "۸۴. انشقاق", "۸۵. بروج", "۸۶. طارق", "۸۷. اعلي",
          "۸۸. غاشيه", "۸۹. فجر", "۹۰. بلد", "۹۱. شمس", "۹۲. ليل", "۹۳. ضحي", "۹۴. انشراح", "۹۵. تين", "۹۶. علق",
          "۹۷. قدر", "۹۸. بينه", "۹۹. زلزله", "۱۰۰. عاديات", "۱۰۱. قارعه", "۱۰۲. تکاثر", "۱۰۳. عصر", "۱۰۴. همزه",
          "۱۰۵. فيل", "۱۰۶. قريش", "۱۰۷. ماعون", "۱۰۸. کوثر", "۱۰۹. کافرون", "۱۱۰. نصر", "۱۱۱. مسد", "۱۱۲. توحيد",
          "۱۱۳. فلق", "۱۱۴. ناس"]


def get_verse_image_url(surah, verse):
    url = CDN_URL + "image/" + str(surah) + "/" + str(verse)
    return url


def get_verse_audio_url(surah, verse, reader_id, quality="high"):
    url = CDN_URL + "audio/" + surah + "/" + reader_id + "/" + str(verse) + "/" + quality
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


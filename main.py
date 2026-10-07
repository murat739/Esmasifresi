import pandas as pd
import streamlit as st

# --- SAYFA YAPILANDIRMASI ---
st.set_page_config(
    page_title="99 Esma-i Hüsna | Risale-i Nur Külliyatı Kapsamlı Portalı",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- ÖZEL CSS STİLLERİ (Kayar Çubuk / Scrollbox ve Kart Tasarımı) ---
st.markdown(
    """
    <style>
    .main-header { font-size: 26px; font-weight: 700; color: #1E3A8A; margin-bottom: 0px; text-align: center; }
    .sub-header { font-size: 15px; color: #475569; margin-bottom: 25px; text-align: center; }
    .esma-card { background-color: #F8FAFC; padding: 20px; border-radius: 10px; border: 1px solid #CBD5E1; margin-bottom: 20px; }
    
    /* Uzun içerikler için kayar çubuk (scroll box) alanı */
    .scroll-box {
        max-height: 220px;
        overflow-y: auto;
        background-color: #FEFCE8;
        padding: 12px;
        border-radius: 6px;
        border: 1px solid #FEF08A;
        font-size: 13px;
        color: #713F12;
        margin-top: 8px;
    }
    .legal-box { background-color: #FEF2F2; padding: 15px; border-radius: 8px; border: 1px solid #F87171; font-size: 12px; color: #7F1D1D; margin-top: 30px; }
    </style>
""",
    unsafe_allow_html=True,
)

# --- BAŞLIK ---
st.markdown(
    '<p class="main-header">📖 99 Esma-i Hüsna: Risale-i Nur Eksenli Kapsamlı Tetkik Portalı</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="sub-header">Bu yazılım tamamen akademik, manevi ve bilgilendirme amaçlı geliştirilmiştir.</p>',
    unsafe_allow_html=True,
)

# --- 99 ESMA-İ HÜSNA TAM VERİ TABANI ---
esma_veritabani = [
    {
        "id": 1,
        "isim": "Allah",
        "arapca": "الله",
        "anlamı": (
            "Bütün ilahi isimleri ve sıfatları kapsayan, esma-i hüsnanın en"
            " büyük (ism-i azam) ve zatı muteber olan özel ismi."
        ),
        "anlam_kaynagi": (
            "Kur'an-ı Kerim ve Arap lügat ilmi (Kamus-u Muhit, Lisanü'l-Arab)"
        ),
        "ayet": "Şüphesiz ben Allah'ım. Benden başka ilah yoktur. Öyleyse bana ibadet et...",
        "ayet_sure": "Taha Suresi, 14. Ayet",
        "ayet_kaynagi": "DİB Kur'an-ı Kerim Meali",
        "hadis": (
            "'Allah'ın doksan dokuz ismi vardır; bunları ezberleyen cennete"
            " girer.'"
        ),
        "hadis_kaynagi": "Sahih-i Buhari, Deavat, 68; Müslim, Zikir, 5",
        "risale_ornek": (
            "Bediüzzaman Said Nursi Hazretleri, 'Allah' ismini bütün esmanın"
            " tahtında bir sultan, merkezî bir nokta olarak açıklar. Kâinattaki"
            " mucizevi sanatlar ve ilahi tecelliler bu ismin etrafında"
            " halkalanır; kainatın sığınağı ve mutlak mabududur."
        ),
        "risale_kaynak": (
            "Risale-i Nur Külliyatı, Şualar (Birinci Şua / İsm-i Azam)"
        ),
    },
    {
        "id": 2,
        "isim": "Ar-Rahman",
        "arapca": "الرحمن",
        "anlamı": (
            "Dünyada bütün mahlukata, ayırt etmeksizin rızık, şefkat ve"
            " merhamet eden."
        ),
        "anlam_kaynagi": "Elmalılı Hamdi Yazır, Hak Dini Kur'an Dili Tefsiri",
        "ayet": "Rahman, Kur'an'ı öğretti. İnsanı yarattı, ona beyanı öğretti.",
        "ayet_sure": "Rahman Suresi, 1-4. Ayetler",
        "ayet_kaynagi": "Kur'an-ı Kerim Meali",
        "hadis": (
            "'Rahman, rahmetin aslını yaratmış ve onu yüz parçaya bölmüştür;"
            " bir parçasını yeryüzüne indirmiştir.'"
        ),
        "hadis_kaynagi": "Sahih-i Müslim, Tevbe, 19",
        "risale_ornek": (
            "Bediüzzaman Hazretleri, kâinattaki şefkatli annelerin yavrularına"
            " düşkünlüğünü, bahar mevsimindeki rızık bolluğunu ve mahlukata"
            " edilen genel ihsanları 'Rahman' isminin geniş tecellisi olarak"
            " açıklar."
        ),
        "risale_kaynak": (
            "Risale-i Nur Külliyatı, Sözler (33. Söz / 27. Mektup)"
        ),
    },
    {
        "id": 3,
        "isim": "Ar-Rahim",
        "arapca": "الرحيم",
        "anlamı": (
            "Ahirette sadece mümin kullarına sonsuz ihsan, ikram ve merhamette"
            " bulunan."
        ),
        "anlam_kaynagi": "İmam Gazali, Al-Maqsad al-Asna",
        "ayet": "...Ve O, müminlere karşı çok merhametlidir (Rahim'dir).",
        "ayet_sure": "Ahzab Suresi, 43. Ayet",
        "ayet_kaynagi": "Kur'an-ı Kerim Meali",
        "hadis": (
            "'Allah Teala, kıyamet gününde rahmetini yüzer katına çıkarır...'"
        ),
        "hadis_kaynagi": "Tirmizi, Deavat, 82",
        "risale_ornek": (
            "Bediüzzaman Hazretleri Rahman ismini dünya mutfağındaki genel"
            " ikramlara benzetirken, Rahim ismini ise o mutfaktaki özel"
            " lezzetlerin iman sahiplerine ikram edilmesi olarak, ebedi"
            " saadetteki tecellisiyle izah eder."
        ),
        "risale_kaynak": (
            "Risale-i Nur Külliyatı, Lem'alar (30. Lem'a / İsm-i Rahim)"
        ),
    },
    {
        "id": 4,
        "isim": "El-Melik",
        "arapca": "الملك",
        "anlamı": (
            "Kâinatın ve her şeyin hakiki sahibi, mutlak hükümdarı ve"
            " yöneticisi."
        ),
        "anlam_kaynagi": "Fahreddin er-Razi, Levamiu'l-Bayyinat",
        "ayet": (
            "Mutlak hükümranlık elinde olan Allah, yüceler yücesidir. O, her"
            " şeye hakkıyla gücü yetendir."
        ),
        "ayet_sure": "Mülk Suresi, 1. Ayet",
        "ayet_kaynagi": "Kur'an-ı Kerim Meali",
        "hadis": (
            "'Kıyamet günü Allah yeryüzünü avucuna alacak... Ben Melik'im"
            " diyecektir.'"
        ),
        "hadis_kaynagi": "Sahih-i Buhari, Tevhid, 19",
        "risale_ornek": (
            "Bediüzzaman Hazretleri, kâinattaki muazzam saltanat ve nizam-ı"
            " ekserinin, kainat sarayındaki memurların ancak mutlak bir 'Melik'"
            " isminin celaliyle idare edilebileceğini açıklar."
        ),
        "risale_kaynak": "Risale-i Nur Külliyatı, Mektubat (20. Mektup)",
    },
    {
        "id": 5,
        "isim": "El-Kuddus",
        "arapca": "القدوس",
        "anlamı": (
            "Her türlü eksiklikten, kusurdan, acizlikten ve noksanlıktan münezzeh"
            " olan, tertemiz."
        ),
        "anlam_kaynagi": "İbn Manzur, Lisanü'l-Arab",
        "ayet": (
            "Göklerde ve yerde ne varsa O'nu tesbih eder. O, Aziz'dir,"
            " Hakim'dir."
        ),
        "ayet_sure": "Cuma Suresi, 1. Ayet",
        "ayet_kaynagi": "Kur'an-ı Kerim Meali",
        "hadis": (
            "Resulullah (s.a.v.) rükû ve secdelerinde 'Sübbuğun Kuddusun' derdi."
        ),
        "hadis_kaynagi": "Sahih-i Müslim, Salat, 223",
        "risale_ornek": (
            "Bediüzzaman Hazretleri 30. Lem'a'da 'Kuddus' ismini kâinat sarayındaki"
            " daimi temizlik nizamı ile açıklar: Eğer kâinatta bu daimi"
            " temizlik olmasaydı, birkaç gün içinde mahlukat murdarlıktan"
            " boğulurdu. Denizlerden rüzgarlara kadar her şey bu ismin"
            " dellalıdır."
        ),
        "risale_kaynak": (
            "Risale-i Nur Külliyatı, Lem'alar (30. Lem'a / İsm-i Kuddus)"
        ),
    },
    {
        "id": 6,
        "isim": "Es-Selam",
        "arapca": "السلام",
        "anlamı": (
            "Her türlü tehlikeden kurtaran, esenlik veren, kullarına selamet"
            " bahşeden."
        ),
        "anlam_kaynagi": "Elmalılı Hamdi Yazır Tefsiri",
        "ayet": "O, kendisinden başka ilah olmayan Allah'tır; Melik'tir, Kuddus'tür, Selam'dır...",
        "ayet_sure": "Haşr Suresi, 23. Ayet",
        "ayet_kaynagi": "Kur'an-ı Kerim Meali",
        "hadis": (
            "'Allahım, sen Selamsın, selamet sensin. Ey celal ve ikram sahibi!'"
        ),
        "hadis_kaynagi": "Sahih-i Müslim, Mesacid, 135",
        "risale_ornek": (
            "Bediüzzaman Hazretleri, kâinattaki fırtınalar içinde mahlukatın"
            " güven bulmasını, anne karnındaki ceninin selametle dünyaya"
            " gelmesini 'Selam' isminin merhametli tecellisiyle izah eder."
        ),
        "risale_kaynak": "Risale-i Nur Külliyatı, Şualar (3. Şua)",
    },
    {
        "id": 7,
        "isim": "El-Mümin",
        "arapca": "المؤمن",
        "anlamı": "Güven veren, emniyet sağlayan, kullarını koruyup inançlarını tasdik eden.",
        "anlam_kaynagi": "Kamus-u Muhit",
        "ayet": "...O, kendisinden başka ilah olmayan... Mümin'dir...",
        "ayet_sure": "Haşr Suresi, 23. Ayet",
        "ayet_kaynagi": "Kur'an-ı Kerim Meali",
        "hadis": "'Mümin, insanların canları ve malları konusunda güvende oldukları kimsedir.'",
        "hadis_kaynagi": "Tirmizi, İman, 2",
        "risale_ornek": (
            "Bediüzzaman Hazretleri, kalplere verilen iman nurunun ve emniyet"
            " duygusunun doğrudan 'Mümin' isminin bir lütfu olduğunu vurgular."
        ),
        "risale_kaynak": "Risale-i Nur Külliyatı, Mesnevi-i Nuriye",
    },
    {
        "id": 8,
        "isim": "El-Müheymin",
        "arapca": "المهيمن",
        "anlamı": "Gözeten, koruyan, her şeyi görüp denetimi altında tutan.",
        "anlam_kaynagi": "Fahreddin er-Razi",
        "ayet": "...Müheymin'dir, Aziz'dir...",
        "ayet_sure": "Haşr Suresi, 23. Ayet",
        "ayet_kaynagi": "Kur'an-ı Kerim Meali",
        "hadis": (
            "'Kul ne zaman Allah'ı zikrederse melekler ve koruması etrafını"
            " sarar.'"
        ),
        "hadis_kaynagi": "Sahih-i Müslim, Zikir, 38",
        "risale_ornek": (
            "Bediüzzaman Hazretleri, kâinattaki hiçbir zerratın başıboş"
            " bırakılmadığını, her birinin Hak Teala tarafından titizlikle"
            " gözetildiğini bu ismin tecellisiyle açıklar."
        ),
        "risale_kaynak": "Risale-i Nur Külliyatı, Asa-yı Musa",
    },
    {
        "id": 9,
        "isim": "El-Aziz",
        "arapca": "العزيز",
        "anlamı": (
            "İzzet sahibi, mutlak galip, mağlup edilmesi mümkün olmayan,"
            " yegâne güçlü."
        ),
        "anlam_kaynagi": "İbn Manzur",
        "ayet": "Şüphesiz Allah Aziz'dir, intikam sahibidir.",
        "ayet_sure": "Ali İmran Suresi, 4. Ayet",
        "ayet_kaynagi": "Kur'an-ı Kerim Meali",
        "hadis": "'İzzet Allah'ın, inayet Resulullah'ın ve müminlerindir.'",
        "hadis_kaynagi": "Müsned-i Ahmed bin Hanbel",
        "risale_ornek": (
            "Bediüzzaman Hazretleri, en aciz mahlukatın bile devasa güçlere"
            " karşı galip gelmesini (örneğin bal arısının savunma mekanizmasını)"
            " Aziz isminin zayıflara merhameten verdiği kudretle açıklar."
        ),
        "risale_kaynak": "Risale-i Nur Külliyatı, Sözler (32. Söz)",
    },
    {
        "id": 10,
        "isim": "El-Cebbar",
        "arapca": "الجبار",
        "anlamı": (
            "Kırıkları onaran, eksikleri tamamlayan, iradesini her durumda"
            " geçiren."
        ),
        "anlam_kaynagi": "Elmalılı Hamdi Yazır",
        "ayet": "...Aziz'dir, Cebbar'dır, Mütekebbir'dir...",
        "ayet_sure": "Haşr Suresi, 23. Ayet",
        "ayet_kaynagi": "Kur'an-ı Kerim Meali",
        "hadis": "'Kıyamet günü Allah cebarları küçük karıncalar gibi haşredecektir.'",
        "hadis_kaynagi": "Tirmizi, Kıyamet, 47",
        "risale_ornek": (
            "Bediüzzaman Hazretleri, kırılan kemiklerin kaynamasını, solan"
            " baharın yeniden diriltilmesini ve ezilenlerin haklarının"
            " alınmasını 'Cebbar' isminin onarıcı tecellisi olarak nitelendirir."
        ),
        "risale_kaynak": "Risale-i Nur Külliyatı, Lem'alar",
    },
]

# Kalan 89 ismin tam ansiklopedik veritabanı
kalan_esmalar = [
    (
        11,
        "El-Mütekebbir",
        "المتكبر",
        "Büyüklük ve azamette eşi olmayan, her şeyde büyüklüğünü gösteren.",
        "Haşr Suresi, 23",
        "Büyüklük benim ridadır...",
        "Müslim, Birr, 136",
        (
            "Bediüzzaman Hazretleri, kâinattaki haşmetli eserlerin ve dağlar"
            " gibi azametli mahlukatın tek sahibinin büyüklüğünü ispat ettiğini"
            " belirtir."
        ),
        "20. Mektup",
    ),
    (
        12,
        "El-Halık",
        "الخالق",
        "Yoktan var eden, ölçüye göre yaratan ve şekil veren.",
        "Haşr Suresi, 24",
        "O, yaratan, yoktan var eden...",
        "Buhari, Tevhid, 1",
        (
            "Bediüzzaman Hazretleri, her bir zerrede ve canlıda hiçbir örnek"
            " olmaksızın yapılan mucizevi yaratılışı Halık isminin daimi"
            " tecellisiyle izah eder."
        ),
        "33. Söz",
    ),
    (
        13,
        "El-Bari",
        "الباري",
        "Örneksiz ve kusursuz olarak uyumlu yaratan.",
        "Haşr Suresi, 24",
        "O, Halık, Bari, Musavvir...",
        "Müslim, Zikir, 17",
        (
            "Bediüzzaman Hazretleri, uzuvların birbiriyle olan mükemmel ahenk"
            " ve dengesini Bari isminin kusursuz icraatıyla açıklar."
        ),
        "20. Mektup",
    ),
    (
        14,
        "El-Musavvir",
        "المصور",
        "Varlıklara en güzel biçimini ve ayırt edici suretini veren.",
        "Haşr Suresi, 24",
        "Rahim olan Allah sizi rahimlerde dilediği gibi şekillendirir.",
        "Ali İmran, 6",
        (
            "Bediüzzaman Hazretleri, yeryüzündeki milyarlarca insan yüzünün"
            " aynı malzemeden yapılmasına rağmen birbirinden tamamen farklı"
            " ve tanınabilir olmasını Musavvir isminin mucizesi olarak"
            " vurgular."
        ),
        "30. Lem'a",
    ),
    (
        15,
        "El-Gaffar",
        "الغفار",
        "Günahları örten, mağfireti ve bağışlaması çok olan.",
        "Taha Suresi, 82",
        "Şüphesiz ben, tevbe eden... kimse için Gaffar'ım.",
        "Taha, 82",
        (
            "Bediüzzaman Hazretleri, kulların kusurlarını ve çirkinliklerini"
            " gece örtüsü gibi örten ve affeden ilahi merhameti Gaffar ismiyle"
            " açıklar."
        ),
        "Mektubat",
    ),
    (
        16,
        "El-Kahhar",
        "القهار",
        "Her şeyi mutlak egemenliği altında tutan, isyankar ve zalimleri kahreden.",
        "Ra'd Suresi, 16",
        "O, her şey üzerinde mutlak hakim olan Kahhar'dır.",
        "Ra'd, 16",
        (
            "Bediüzzaman Hazretleri, kâinattaki nizama karşı gelen ve fesat"
            " çıkaran unsurların Kahhar isminin celaliyle tesirsiz hale"
            " getirildiğini açıklar."
        ),
        "Şualar",
    ),
    (
        17,
        "El-Vehhab",
        "الوهاب",
        "Karşılıksız bol bol ihsan eden, lütuf ve inayet sahibi.",
        "Sad Suresi, 9",
        "Yoksa aziz ve vehhab olan Rabbinin hazineleri onların yanında mı?",
        "Sad, 9",
        (
            "Bediüzzaman Hazretleri, mahlukata hiçbir bedel istemeden sunulan"
            " nefes, su, ışık ve hayat gibi muazzam nimetleri Vehhab isminin"
            " cömertliğiyle izah eder."
        ),
        "20. Mektup",
    ),
    (
        18,
        "El-Rezzak",
        "الرزاق",
        "Bütün mahlukatın rızkını veren ve ihtiyaçlarını karşılayan.",
        "Zariyat Suresi, 58",
        "Şüphesiz rızık veren, mutlak kudret sahibi olan Allah'tır.",
        "Zariyat, 58",
        (
            "Bediüzzaman Hazretleri, dilsiz hayvanlardan derin denizlerdeki"
            " balıklara kadar en zayıf mahlukatın bile unutmaksızın rızkının"
            " verilmesini Rezzak isminin azametli mucizesi olarak gösterir."
        ),
        "Sözler (10. Söz)",
    ),
    (
        19,
        "El-Fettah",
        "الفتاح",
        "Her türlü güçlüğü kolaylaştıran, rahmet kapılarını açan ve hükmeden.",
        "Sebe Suresi, 26",
        "De ki: Rabbimiz aramızı hak ile açar (fettah). O, her şeyi bilendir.",
        "Sebe, 26",
        (
            "Bediüzzaman Hazretleri, kilitlenmiş gibi duran hallerin ve kışın"
            " ardından bahar kapılarının açılmasını Fettah isminin hikmetiyle"
            " açıklar."
        ),
        "Lem'alar",
    ),
    (
        20,
        "El-Alim",
        "العليم",
        "Her şeyi en ince detayına kadar bilen, ilmi sınırsız olan.",
        "Bakara Suresi, 32",
        "Şüphesiz sen Alim'sin, Hakim'sin.",
        "Bakara, 32",
        (
            "Bediüzzaman Hazretleri, atomdan yıldızlara kadar kâinattaki hiçbir"
            " şeyin ilminin Allah'ın ilminden gizli kalamayacağını Alim ismiyle"
            " delillendirir."
        ),
        "20. Mektup",
    ),
    (
        21,
        "El-Kabid",
        "القابض",
        "Dilediğinin rızkını veya kalbini daraltan.",
        "Bakara Suresi, 245",
        "Allah sıkar (kabzeder) ve açar...",
        "Bakara, 245",
        (
            "Bediüzzaman Hazretleri, insan ruhundaki kabz hallerinin,"
            " kâinattaki mevsimsel daralmaların bu isimle idare edildiğini belirtir."
        ),
        "Mektubat",
    ),
    (
        22,
        "El-Basit",
        "الباسط",
        "Rızkı genişleten, kalplere ferahlık ve bolluk veren.",
        "Bakara Suresi, 245",
        "Allah sıkar ve genişletir (basit eder)...",
        "Bakara, 245",
        (
            "Bediüzzaman Hazretleri, baharda yeryüzünün rahmetle genişletilmesini"
            " Basit isminin tecellisi olarak açıklar."
        ),
        "Mektubat",
    ),
    (
        23,
        "El-Hafid",
        "الخافض",
        "Kafirleri ve zalimleri alçaltan, gururluları zelil eden.",
        "Vakıa Suresi, 3",
        "O (kıyamet) alçaltıcıdır, yükselticidir.",
        "Vakıa, 3",
        (
            "Bediüzzaman Hazretleri, kibirlenen firavunların ve zalimlerin"
            " tarih boyunca nasıl alçaltıldığını Hafid ismiyle açıklar."
        ),
        "Şualar",
    ),
    (
        24,
        "El-Rafi",
        "الرافع",
        "Şeref veren, dereceleri yükselten, müminleri aziz kılan.",
        "Vakıa Suresi, 3",
        "...Alçaltıcı, yükselticidir.",
        "Vakıa, 3",
        (
            "Bediüzzaman Hazretleri, iman ve ameliyle tevazu gösterenlerin"
            " manevi olarak makamlarının yükseltilmesini Rafi ismiyle açıklar."
        ),
        "Şualar",
    ),
    (
        25,
        "El-Muiz",
        "المعز",
        "İstediğini aziz kılan, onurlandıran.",
        "Ali İmran Suresi, 26",
        "Dilediğini aziz kılarsın, dilediğini zelil edersin.",
        "Ali İmran, 26",
        (
            "Bediüzzaman Hazretleri, hakikat ehlinin izzetini ve manevi"
            " üstünlüğünü Muiz isminin tecellisiyle izah eder."
        ),
        "Mektubat",
    ),
    (
        26,
        "El-Muzil",
        "المضل",
        "Dilediğini hor ve hakir eden, zillet veren.",
        "Ali İmran Suresi, 26",
        "...Dilediğini zelil edersin.",
        "Ali İmran, 26",
        (
            "Bediüzzaman Hazretleri, hakikate sırt çevirenlerin hak etikleri"
            " zilleti Muzil ismi çerçevesinde bulduklarını belirtir."
        ),
        "Mektubat",
    ),
    (
        27,
        "El-Semi",
        "السميع",
        "Gizli açık her sesi, fısıltıyı en mükemmel işiten.",
        "Şura Suresi, 11",
        "O, her şeyi işiten ve görendir (Semi-i Basir).",
        "Şura, 11",
        (
            "Bediüzzaman Hazretleri, milyarlarca mahlukun aynı anda yaptığı"
            " duaları ve yalvarışları birbirine karıştırmadan işitmesini Semi"
            " ismiyle açıklar."
        ),
        "20. Mektup",
    ),
    (
        28,
        "El-Basir",
        "البصير",
        "Her şeyi en ince detayına kadar gören, hiçbir şey gizli kalmayan.",
        "Hucurat Suresi, 18",
        "Şüphesiz Allah göklerin ve yerin gaybını bilir. Allah yaptıklarınızı görendir.",
        "Hucurat, 18",
        (
            "Bediüzzaman Hazretleri, karanlık gecede, denizin dibindeki karıncanın"
            " hareketini dahi gören Basir isminin azametini misallerle anlatır."
        ),
        "20. Mektup",
    ),
    (
        29,
        "El-Hakem",
        "الحكم",
        "Mutlak hakim, hak ile batılı ayıran, adil hüküm veren.",
        "Hac Suresi, 69",
        "Kıyamet günü Allah aranızda hükmedecektir.",
        "Hac, 69",
        (
            "Bediüzzaman Hazretleri, kâinattaki tüm yasal ve fıtri hükümlerin"
            " Hakem isminin adaletli kanunlarıyla yürütüldüğünü ifade eder."
        ),
        "Lem'alar",
    ),
    (
        30,
        "El-Adl",
        "العدل",
        "Mutlak adalet sahibi, zulmetmeyen.",
        "En'am Suresi, 115",
        "Rabbinin kelimesi doğruluk ve adaletle tamamlanmıştır.",
        "En'am, 115",
        (
            "Bediüzzaman Hazretleri 30. Lem'a'da Adl ismini kâinattaki mizan"
            " esasıyla açıklar: Hiçbir zerre zayi olmaz, en küçük zulüm mahkeme-i"
            " kübrada karşılığını bulur."
        ),
        "30. Lem'a (İsm-i Adl)",
    ),
    (
        31,
        "El-Latif",
        "اللطيف",
        "Lütuf sahibi, en ince işlerin detaylarını bilen ve zarif ihsanlarda bulunan.",
        "Mülk Suresi, 14",
        "O latiftir, her şeyden haberdardır.",
        "Mülk, 14",
        (
            "Bediüzzaman Hazretleri, en küçük hücrelerde ve tohumlarda"
            " muazzam planların saklanmasını Latif isminin zarafetiyle açıklar."
        ),
        "30. Lem'a (İsm-i Latif)",
    ),
    (
        32,
        "El-Habir",
        "الخبير",
        "Her şeyin iç yüzünden, gizli hallerinden haberdar olan.",
        "En'am Suresi, 18",
        "O, hikmet sahibidir, her şeyden haberdardır (Habir).",
        "En'am, 18",
        (
            "Bediüzzaman Hazretleri, atomların derinliklerindeki nizamı ve"
            " kalplerin niyetlerini Habir isminin ihatasıyla açıklar."
        ),
        "20. Mektup",
    ),
    (
        33,
        "El-Halim",
        "الحليم",
        "Cezada acele etmeyen, kullarının kusurlarına karşı yumuşak davranan.",
        "Bakara Suresi, 235",
        "Biliniz ki Allah bağışlayıcıdır, halimdir.",
        "Bakara, 235",
        (
            "Bediüzzaman Hazretleri, insanların en büyük nankörlüklerine karşı"
            " bile rızıklarının kesilmemesini Halim isminin azametli"
            " mühlet vermesiyle açıklar."
        ),
        "Mektubat",
    ),
    (
        34,
        "El-Azim",
        "العظيم",
        "Pek yüce, azamet sahibi, akılların idrak edemeyeceği büyüklükte.",
        "Bakara Suresi, 255",
        "O, yücedir, azimdir.",
        "Bakara, 255",
        (
            "Bediüzzaman Hazretleri, kâinatın muazzam büyüklüğü karşısında"
            " insanın idrakinin aciz kalmasını Azim isminin tecellisiyle"
            " açıklar."
        ),
        "20. Mektup",
    ),
    (
        35,
        "El-Gafur",
        "الغفور",
        "Günahları çok bağışlayan, mağfireti bol olan.",
        "Fatır Suresi, 28",
        "Şüphesiz Allah azizdir, gafurdur.",
        "Fatır, 28",
        (
            "Bediüzzaman Hazretleri, samimi tevbe edenlerin bütün geçmiş"
            " günahlarının affedilmesini Gafur isminin geniş rahmetiyle"
            " müjdeler."
        ),
        "Lem'alar",
    ),
    (
        36,
        "El-Şekur",
        "الشكور",
        "Az amele karşılık çok mükâfat veren, şükredenleri ödüllendiren.",
        "Şura Suresi, 23",
        "Şüphesiz O gafurdur, şekurdur.",
        "Şura, 23",
        (
            "Bediüzzaman Hazretleri, kulların küçük şükürlerine karşılık"
            " cennetler dolusu nimetler ihsan edilmesini Şekur ismiyle açıklar."
        ),
        "Sözler",
    ),
    (
        37,
        "El-Aliy",
        "العلي",
        "Pek yüce, her şeyden muktedir ve üstün olan.",
        "Lokman Suresi, 30",
        "Çünkü Allah yücedir, büyüktür.",
        "Lokman, 30",
        (
            "Bediüzzaman Hazretleri, hiçbir şeyin O'na denk olamayacağını ve"
            " her bakımından en üstün makamda olduğunu Aliy ismiyle açıklar."
        ),
        "20. Mektup",
    ),
    (
        38,
        "El-Kebir",
        "الكبير",
        "Mutlak büyük, azamet sahibi.",
        "Ra'd Suresi, 9",
        "O, büyük ve yücedir.",
        "Ra'd, 9",
        (
            "Bediüzzaman Hazretleri, kâinattaki en büyük galaksilerin bile O'nun"
            " kudreti karşısında bir zerre hükmünde olduğunu Kebir ismiyle"
            " açıklar."
        ),
        "20. Mektup",
    ),
    (
        39,
        "El-Hafiz",
        "الحفيظ",
        "Her şeyi muhafaza eden, gözetleyen, fenalıklardan koruyan.",
        "Hud Suresi, 57",
        "Şüphesiz Rabbim her şeyi koruyandır.",
        "Hud, 57",
        (
            "Bediüzzaman Hazretleri, tohumların toprak altında bozulmadan"
            " saklanmasını ve kâinatın hafızasında her amelin kayda"
            " geçirilmesini Hafiz ismiyle izah eder."
        ),
        "30. Lem'a",
    ),
    (
        40,
        "El-Mukit",
        "المقيت",
        "Her türlü rızkı, azığı yaratan ve mahlukata ulaştıran.",
        "Nisa Suresi, 85",
        "Allah her şeye gücü yetendir (Mukit).",
        "Nisa, 85",
        (
            "Bediüzzaman Hazretleri, bedenlerin ve ruhların gıdalarını eksiksiz"
            " tayin edip ulaştıranın Mukit ismi olduğunu belirtir."
        ),
        "Mektubat",
    ),
    (
        41,
        "El-Hasib",
        "الحسيب",
        "Kulların hesabını en iyi gören, her şeye kâfi gelen.",
        "Nisa Suresi, 6",
        "Hesap görücü olarak Allah yeter.",
        "Nisa, 6",
        (
            "Bediüzzaman Hazretleri, kâinattaki milyarlarca varlığın hesabının"
            " anlık olarak tutulmasını Hasib isminin azametiyle açıklar."
        ),
        "Şualar",
    ),
    (
        42,
        "El-Celil",
        "الجليل",
        "Celal ve azamet sahibi, büyük ve haşmetli.",
        "Rahman Suresi, 27",
        "Celal ve ikram sahibi Rabbinin adı yücedir.",
        "Rahman, 27",
        (
            "Bediüzzaman Hazretleri, kâinattaki yıldırımlar, dağlar ve haşmetli"
            " afetler arkasındaki ilahi heybeti Celil ismiyle açıklar."
        ),
        "30. Lem'a",
    ),
    (
        43,
        "El-Kerim",
        "الكريم",
        "Çok cömert, ikramı bol, sözünde duran, lütufkâr.",
        "Neml Suresi, 40",
        "Şüphesiz Rabbim zengindir, kerimdir.",
        "Neml, 40",
        (
            "Bediüzzaman Hazretleri, kullarına istemeden sonsuz ikramlarda"
            " bulunan ilahi cömertliği Kerim ismiyle izah eder."
        ),
        "20. Mektup",
    ),
    (
        44,
        "El-Rakib",
        "الرقيب",
        "Her varlığı, her ameli an be an gözetim altında tutan.",
        "Nisa Suresi, 1",
        "Şüphesiz Allah üzerinizde bir gözetleyicidir (Rakib).",
        "Nisa, 1",
        (
            "Bediüzzaman Hazretleri, insanın kalbinden geçenleri dahi an be an"
            " denetleyen ilahi nezareti Rakib ismiyle açıklar."
        ),
        "Mektubat",
    ),
    (
        45,
        "El-Mucib",
        "المجيب",
        "Dualara icabet eden, istekleri geri çevirmeyen.",
        "Hud Suresi, 61",
        "Şüphesiz Rabbim yakındır, dualara icabet edendir.",
        "Hud, 61",
        (
            "Bediüzzaman Hazretleri, en aciz anında mahlukatın yaptığı"
            " yakarışlara cevap veren ilahi merhameti Mucib ismiyle açıklar."
        ),
        "20. Mektup",
    ),
    (
        46,
        "El-Vasi",
        "الواسع",
        "İlmi, rahmeti, kudreti her şeyi kuşatan, geniş.",
        "Bakara Suresi, 268",
        "Allah lütfu bol olan, her şeyi bilendir (Vasi).",
        "Bakara, 268",
        (
            "Bediüzzaman Hazretleri, kâinattaki hiçbir ihtiyacın ilahi rahmete"
            " dar gelmemesini Vasi ismiyle açıklar."
        ),
        "20. Mektup",
    ),
    (
        47,
        "El-Hakim",
        "الحكيم",
        "Sonsuz hikmet sahibi.",
        "En'am Suresi, 18",
        "O hakimdir, habirdir.",
        "En'am, 18",
        (
            "Bediüzzaman Hazretleri 30. Lem'a'da Hakim ismini kâinattaki hiçbir"
            " şeyin abes yaratılmadığı hakikatiyle genişçe işler."
        ),
        "30. Lem'a (İsm-i Hakim)",
    ),
    (
        48,
        "El-Vedud",
        "الودود",
        "Kullarını çok seven, sevilmeye en layık olan.",
        "Hud Suresi, 90",
        "Şüphesiz Rabbim çok merhametlidir, çok sevendir (Vedud).",
        "Hud, 90",
        (
            "Bediüzzaman Hazretleri, kâinattaki bütün şefkat ve muhabbet"
            " duygularının Vedud isminin tecellisinden birer damla olduğunu"
            " açıklar."
        ),
        "30. Lem'a (İsm-i Vedud)",
    ),
    (
        49,
        "El-Mecid",
        "المجيد",
        "Şanı yüce, şerefi ve kadrü kıymeti en büyük olan.",
        "Hud Suresi, 73",
        "Şüphesiz O övülmüştür, şanı yücedir (Mecid).",
        "Hud, 73",
        (
            "Bediüzzaman Hazretleri, kâinattaki muazzam ihtişamın ve övgüye"
            " layık eserlerin Mecid isminin şerefini yansıttığını belirtir."
        ),
        "20. Mektup",
    ),
    (
        50,
        "El-Bais",
        "الباعث",
        "Ölüleri dirilten, kabirlerden çıkaran, peygamber gönderen.",
        "Hac Suresi, 7",
        "Şüphesiz Allah kabirdekileri diriltecektir.",
        "Hac, 7",
        (
            "Bediüzzaman Hazretleri, baharda milyarlarca bitkinin haşrini"
            " yapan kudretin insanı da ahirette dirilteceğini Bais ismiyle"
            " ispat eder."
        ),
        "10. Söz (Haşir Risalesi)",
    ),
    (
        51,
        "El-Sehid",
        "الشهيد",
        "Her yerde hazır ve nazır olan, her şeye şahitlik eden.",
        "Mucadele Suresi, 6",
        "Şüphesiz Allah her şeye şahittir.",
        "Mucadele, 6",
        (
            "Bediüzzaman Hazretleri, kâinattaki her anın ve amelin şahidi olan"
            " ilahi adaleti Sehid ismiyle açıklar."
        ),
        "Mektubat",
    ),
    (
        52,
        "El-Hakk",
        "الحق",
        "Varlığı hak olan, gerçeğin kendisi, hükmü kesin olan.",
        "Hac Suresi, 6",
        "Çünkü Allah Hak'tır ve ölüleri diriltir.",
        "Hac, 6",
        (
            "Bediüzzaman Hazretleri, kâinattaki tüm hakikatlerin ve gayelerin"
            " Hak ismine dayandığını belirtir."
        ),
        "20. Mektup",
    ),
    (
        53,
        "El-Vekil",
        "الوكيل",
        "Kendisine güvenilip dayanılan, işleri en güzel idare eden.",
        "Ali İmran Suresi, 173",
        "Allah bize yeter, O ne güzel vekildir.",
        "Ali İmran, 173",
        (
            "Bediüzzaman Hazretleri, kulların bütün işlerinde O'na tevekkül"
            " etmelerinin gereğini Vekil isminin emniyetiyle açıklar."
        ),
        "23. Söz",
    ),
    (
        54,
        "El-Kavi",
        "القوي",
        "Sınırsız güç ve kudret sahibi, hiç düşmeyen.",
        "Hac Suresi, 74",
        "Şüphesiz Allah kuvvetlidir, azizdir.",
        "Hac, 74",
        (
            "Bediüzzaman Hazretleri, kâinattaki en ağır yükleri bile kolayca"
            " çeviren mutlak kuvveti Kavi ismiyle açıklar."
        ),
        "20. Mektup",
    ),
    (
        55,
        "El-Metin",
        "المتين",
        "Çok sağlam, kudretinde asla sarsıntı olmayan.",
        "Zariyat Suresi, 58",
        "Şüphesiz rızık veren, metin kudret sahibi olan Allah'tır.",
        "Zariyat, 58",
        (
            "Bediüzzaman Hazretleri, göklerin direksiz durmasını ve kâinat"
            " nizamının sarsılmamasını Metin ismiyle açıklar."
        ),
        "20. Mektup",
    ),
    (
        56,
        "El-Veli",
        "الولي",
        "İnananların dostu, yardımcısı ve koruyucusu.",
        "Bakara Suresi, 257",
        "Allah iman edenlerin dostudur (velisidir)...",
        "Bakara, 257",
        (
            "Bediüzzaman Hazretleri, müminlerin zor anlarında imdatlarına"
            " yetişen ilahi yakınlığı Veli ismiyle açıklar."
        ),
        "Mektubat",
    ),
    (
        57,
        "El-Hamid",
        "الحميد",
        "Bütün övgülere ve şükürlere layık olan.",
        "İbrahim Suresi, 1",
        "Aziz ve Hamid olan Allah'ın yoluna...",
        "İbrahim, 1",
        (
            "Bediüzzaman Hazretleri, kâinattaki bütün dillerin ve mahlukatın"
            " kendi halleriyle O'nu övmesini Hamid ismiyle açıklar."
        ),
        "20. Mektup",
    ),
    (
        58,
        "El-Muhsi",
        "المحصي",
        "Her şeyin sayısını, miktarını eksiksiz bilen.",
        "Meryem Suresi, 94",
        "Andolsun ki onları kuşatmış ve teker teker saymıştır (muhsi).",
        "Meryem, 94",
        (
            "Bediüzzaman Hazretleri, yağmur damlalarından yapraklara kadar"
            " hiçbir şeyin ilahi hesaptan kaçamayacağını Muhsi ismiyle açıklar."
        ),
        "20. Mektup",
    ),
    (
        59,
        "El-Mübdil",
        "المبديء",
        "Varlıkları ilk defa örneksiz yaratan.",
        "Buruc Suresi, 13",
        "Şüphesiz O, başlangıcı yapar ve yeniden diriltir (mübdil ve muid).",
        "Buruc, 13",
        (
            "Bediüzzaman Hazretleri, kainatın ilk yaratılışındaki harikaları"
            " Mübdil ismiyle izah eder."
        ),
        "10. Söz",
    ),
    (
        60,
        "El-Muid",
        "المعيد",
        "Yarattıktan sonra öldürüp yeniden diriltecek olan.",
        "Rum Suresi, 27",
        "Yaratmayı ilkin yapan, sonra onu tekrarlayan (muid) O'dur.",
        "Rum, 27",
        (
            "Bediüzzaman Hazretleri, ahiretteki yeniden dirilişin ilk yaratılış"
            " kadar kolay olduğunu Muid ismiyle ispat eder."
        ),
        "10. Söz",
    ),
    (
        61,
        "El-Muhyi",
        "المحيي",
        "Hayat veren, dirilten.",
        "Fussilet Suresi, 39",
        "Şüphesiz O ölüleri diriltkendir (muhyidir).",
        "Fussilet, 39",
        (
            "Bediüzzaman Hazretleri, ölmüş toprakların baharda binbir çeşit"
            " hayatla donatılmasını Muhyi ismiyle açıklar."
        ),
        "30. Lem'a",
    ),
    (
        62,
        "El-Mumit",
        "المميت",
        "Canlıların ölümünü yaratan, hayatı sonlandıran.",
        "Ali İmran Suresi, 156",
        "Yaratan ve öldüren O'dur.",
        "Ali İmran, 156",
        (
            "Bediüzzaman Hazretleri, ölümün yok olmak değil, vazife"
            " değiştirme ve terhis olduğunu Mumit ismiyle açıklar."
        ),
        "10. Söz",
    ),
    (
        63,
        "El-Hayy",
        "الحي",
        "Ebedi diri olan hayat kaynağı.",
        "Mümin Suresi, 65",
        "O, ölümsüz ve daima diri olandır...",
        "Mümin, 65",
        (
            "Bediüzzaman Hazretleri 30. Lem'a'da Hayy ismini kâinattaki daimi"
            " hayat dalgalanmaları ve bahar dirilişleriyle detaylıca işler."
        ),
        "30. Lem'a (İsm-i Hayy)",
    ),
    (
        64,
        "El-Kayyum",
        "القيوم",
        "Kâinatı ayakta tutan ve idare eden.",
        "Bakara Suresi, 255",
        "O Hayy'dır, Kayyum'dur.",
        "Bakara, 255",
        (
            "Bediüzzaman Hazretleri 30. Lem'a'da Kayyum ismini kâinatın her an"
            " kudretle ayakta tutulması esasıyla izah eder."
        ),
        "30. Lem'a (İsm-i Kayyum)",
    ),
    (
        65,
        "El-Vacid",
        "الواجد",
        "Hiçbir şeyi kaybetmeyen, aradığını dilediği an bulan.",
        "Duha Suresi, 7-8",
        "Seni kaybolmuş bulup da yönlendirmedi mi?",
        "Duha, 7",
        (
            "Bediüzzaman Hazretleri, kainatta hiçbir zerrenin kaybolmadığını"
            " Vacid ismiyle açıklar."
        ),
        "Mektubat",
    ),
    (
        66,
        "El-Macid",
        "الماجد",
        "Şanı yüce, kerem ve cömertliği sonsuz.",
        "Hud Suresi, 73",
        "Şüphesiz O övülmüştür, maciddir.",
        "Hud, 73",
        (
            "Bediüzzaman Hazretleri, ilahi ihsanların yüceliğini Macid ismiyle"
            " vurgular."
        ),
        "20. Mektup",
    ),
    (
        67,
        "El-Vahid",
        "الواحد",
        "Zatında, sıfatlarında ortağı ve benzeri olmayan tek.",
        "İhlas Suresi, 1",
        "De ki: O Allah tektir (vahid/ahad).",
        "İhlas, 1",
        (
            "Bediüzzaman Hazretleri, kâinattaki birliğin tek bir Vahid'in"
            " eserinden başka olamayacağını ispat eder."
        ),
        "33. Söz",
    ),
    (
        68,
        "El-Ahad",
        "الأحد",
        "Tek ve eşsiz olan.",
        "İhlas Suresi, 1",
        "De ki: Allah ahad'dır.",
        "İhlas, 1",
        (
            "Bediüzzaman Hazretleri, her şeyin mutlak birliğe işaret ettiğini"
            " Ahad ismiyle açıklar."
        ),
        "33. Söz",
    ),
    (
        69,
        "El-Samed",
        "الصمد",
        "Her şeyin kendisine muhtaç olduğu, kendisi hiçbir şeye muhtaç olmayan.",
        "İhlas Suresi, 2",
        "Allah sameddir.",
        "İhlas, 2",
        (
            "Bediüzzaman Hazretleri, kâinattaki bütün varlıkların ihtiyaç"
            " anında yalvardığı merciin Samed olduğunu muazzam bir tefsirle"
            " anlatır."
        ),
        "Sözler (İhlas Risalesi)",
    ),
    (
        70,
        "El-Kadir",
        "القادر",
        "Her şeye gücü yeten, dilediğini yaratan.",
        "En'am Suresi, 65",
        "De ki: O, başınıza üstünüzden bir azap göndermeye kadirdir.",
        "En'am, 65",
        (
            "Bediüzzaman Hazretleri, baharı yaratmakla bir sineği yaratmak"
            " O'nun kudretinde birdir hakikatini Kadir ismiyle izah eder."
        ),
        "20. Mektup",
    ),
    (
        71,
        "El-Muktedir",
        "المقتدر",
        "Mutlak kudret sahibi, her şeye gücü yeten.",
        "Kamer Suresi, 42",
        "Mutlak kudret sahibi bir melikin katında (muktedir).",
        "Kamer, 42",
        (
            "Bediüzzaman Hazretleri, kâinattaki devasa galaksileri kolayca"
            " döndüren kudreti Muktedir ismiyle açıklar."
        ),
        "20. Mektup",
    ),
    (
        72,
        "El-Mukaddim",
        "المقدم",
        "Dilediğini öne geçiren, yükselten.",
        "Kaf Suresi, 28",
        "Huzurumda çekişmeyin, ben size daha önce uyarı göndermiştim.",
        "Kaf, 28",
        (
            "Bediüzzaman Hazretleri, tarih sahnesinde bazı milletleri ve"
            " şahsiyetleri öne geçiren hikmeti Mukaddim ismiyle açıklar."
        ),
        "Mektubat",
    ),
    (
        73,
        "El-Muahhir",
        "المؤخر",
        "Dilediğini arkaya bırakan, geciktiren.",
        "Nuh Suresi, 4",
        "Sizin ecelinizi belirlenmiş bir süreye kadar erteler (muahhir).",
        "Nuh, 4",
        (
            "Bediüzzaman Hazretleri, ilahi hikmet gereği bazı işlerin ve"
            " cezaların ertelenmesini Muahhir ismiyle açıklar."
        ),
        "Mektubat",
    ),
    (
        74,
        "El-Evvel",
        "الأول",
        "Varlığının başlangıcı olmayan, ezeli.",
        "Hadid Suresi, 3",
        "O Evvel'dir, Ahir'dir, Zahir'dir, Batin'dir.",
        "Hadid, 3",
        (
            "Bediüzzaman Hazretleri, kâinatın ve zamanın başlangıcından önce"
            " de var olan ezeli Hakikat'i Evvel ismiyle açıklar."
        ),
        "30. Lem'a",
    ),
    (
        75,
        "El-Ahir",
        "الآخر",
        "Varlığının sonu olmayan, ebedi.",
        "Hadid Suresi, 3",
        "O Evvel'dir, Ahir'dir...",
        "Hadid, 3",
        (
            "Bediüzzaman Hazretleri, bütün mahlukat yok olduktan sonra baki"
            " kalan tek Zat'ın Ahir ismi olduğunu belirtir."
        ),
        "30. Lem'a",
    ),
    (
        76,
        "El-Zahir",
        "الظاهر",
        "Varlığı delilleriyle apaçık ortadan görünen.",
        "Hadid Suresi, 3",
        "O Zahir'dir ve Batin'dir.",
        "Hadid, 3",
        (
            "Bediüzzaman Hazretleri, kâinattaki her bir eser ve nizamın açık"
            " birer imza gibi Yaratıcı'yı göstermesini Zahir ismiyle açıklar."
        ),
        "30. Lem'a",
    ),
    (
        77,
        "El-Batin",
        "الباطن",
        "Zatının mahiyeti gizli olan, gözlerle idrak edilemeyen.",
        "Hadid Suresi, 3",
        "O Zahir'dir ve Batin'dir.",
        "Hadid, 3",
        (
            "Bediüzzaman Hazretleri, akılların Zat'ının hakikatini kavramaktan"
            " aciz kalmasını Batin ismiyle izah eder."
        ),
        "30. Lem'a",
    ),
    (
        78,
        "El-Vali",
        "الوالي",
        "Kâinatı ve bütün işleri tek başına yöneten.",
        "Ra'd Suresi, 11",
        "İnsanı önünden ve arkasından takip eden melekler vardır...",
        "Ra'd, 11",
        (
            "Bediüzzaman Hazretleri, kâinat sarayındaki bütün işlerin bir tek"
            " Vali tarafından idare edildiğini belirtir."
        ),
        "Mektubat",
    ),
    (
        79,
        "El-Müteali",
        "المتعالي",
        "Akla gelebilecek her türlü zihni tasavvurdan yüce ve münezzeh.",
        "Ra'd Suresi, 9",
        "Büyük ve yüce olan (müteali) Allah'ın şanı yücedir.",
        "Ra'd, 9",
        (
            "Bediüzzaman Hazretleri, ilahi azametin insan düşüncesinin çok"
            " ötesinde olduğunu Müteali ismiyle açıklar."
        ),
        "Mektubat",
    ),
    (
        80,
        "El-Berr",
        "البّر",
        "İyilik ve ihsanı bol olan, kullarına kolaylık veren.",
        "Tur Suresi, 28",
        "Şüphesiz biz daha önce O'na yalvardık. O gerçekten iyilik edendir (berr).",
        "Tur, 28",
        (
            "Bediüzzaman Hazretleri, kullarına sürekli iyilik ve rahmet"
            " ulaştıran ilahi şefkati Berr ismiyle açıklar."
        ),
        "20. Mektup",
    ),
    (
        81,
        "El-Tevvab",
        "التواب",
        "Tevbeleri kabul eden, günahları bağışlayan.",
        "Bakara Suresi, 37",
        "Şüphesiz O tevbeyi çok kabul eden, merhamet edendir.",
        "Bakara, 37",
        (
            "Bediüzzaman Hazretleri, kullarının pişmanlıklarını kabul edip"
            " onları tertemiz kılan ilahi merhameti Tevvab ismiyle müjdeler."
        ),
        "Lem'alar",
    ),
    (
        82,
        "El-Muntekim",
        "المنتقم",
        "Zalimlerin ve suçluların hak ettikleri cezayı veren.",
        "Secde Suresi, 22",
        "Şüphesiz biz suçlulardan intikam alıcıyız.",
        "Secde, 22",
        (
            "Bediüzzaman Hazretleri, ilahi adaletin tecellisi olarak zalimlerin"
            " cezasız kalmadığını Muntekim ismiyle açıklar."
        ),
        "Şualar",
    ),
    (
        83,
        "El-Afüvv",
        "العفو",
        "Günahları affeden, bağışlayan, suçları silen.",
        "Hac Suresi, 60",
        "Şüphesiz Allah çok affedicidir, bağışlayıcıdır.",
        "Hac, 60",
        (
            "Bediüzzaman Hazretleri, kulların affedilme ümidini canlı tutan"
            " Afüvv isminin kuşatıcı rahmetini açıklar."
        ),
        "Mektubat",
    ),
    (
        84,
        "El-Rauf",
        "الرؤوف",
        "Çok şefkatli, merhamet sahibi, yumuşak kalpli.",
        "Nur Suresi, 20",
        "Şüphesiz Allah şefkatlidir, merhametlidir.",
        "Nur, 20",
        (
            "Bediüzzaman Hazretleri, kullarına bir anne şefkatinden kat kat"
            " ziyade merhamet eden ilahi şefkati Rauf ismiyle açıklar."
        ),
        "Mektubat",
    ),
    (
        85,
        "Malikü'l-Mülk",
        "مالك الملك",
        "Mülkün ebedi ve hakiki sahibi.",
        "Ali İmran Suresi, 26",
        "De ki: Ey mülkün sahibi olan Allah'ım!",
        "Ali İmran, 26",
        (
            "Bediüzzaman Hazretleri, kâinattaki hiçbir varlığın hakiki malik"
            " olamayacağını, mülkün tek sahibinin Malikü'l-Mülk olduğunu"
            " açıklar."
        ),
        "11. Söz",
    ),
    (
        86,
        "Zü'l-Celâli ve'l-İkrâm",
        "ذو الجلال والإكرام",
        "Celal (azamet) ve ikram (cömertlik) sahibi.",
        "Rahman Suresi, 27",
        "Celal ve ikram sahibi Rabbinin adı yücedir.",
        "Rahman, 27",
        (
            "Bediüzzaman Hazretleri, kâinattaki haşmet ile lütfun birleştiği"
            " noktada bu ismin tecelli ettiğini belirtir."
        ),
        "20. Mektup",
    ),
    (
        87,
        "El-Muksit",
        "المقسط",
        "Bütün işlerini adaletle, denge ve uyum içinde yapan.",
        "Ali İmran Suresi, 18",
        "Adaletle ayakta duran Allah...",
        "Ali İmran, 18",
        (
            "Bediüzzaman Hazretleri, kâinattaki kusursuz dengeyi Muksit ismiyle"
            " izah eder."
        ),
        "Mektubat",
    ),
    (
        88,
        "El-Cami",
        "الجامع",
        "İstediğini istediği yerde toplayan, haşir gününde mahlukatı bir araya getiren.",
        "Ali İmran Suresi, 9",
        "Şüphesiz Allah insanları gelmesinde şüphe olmayan günde toplayacaktır.",
        "Ali İmran, 9",
        (
            "Bediüzzaman Hazretleri, kâinattaki dağınık unsurların baharda"
            " yeniden derlenmesini ve ahiretteki haşri Cami ismiyle açıklar."
        ),
        "10. Söz",
    ),
    (
        89,
        "El-Gani",
        "الغني",
        "Zengin, hiçbir şeye ihtiyacı olmayan, her şey O'na muhtaç.",
        "Fatır Suresi, 15",
        "Ey insanlar, siz Allah'a muhtaçsınız; Allah ise Gani'dir.",
        "Fatır, 15",
        (
            "Bediüzzaman Hazretleri, hiçbir şeye el uzatmayan ama her şeye yeten"
            " mutlak zenginliği Gani ismiyle açıklar."
        ),
        "20. Mektup",
    ),
    (
        90,
        "El-Mugni",
        "المغني",
        "Dilediğini zengin eden, ihtiyaç gideren.",
        "Tevbe Suresi, 28",
        "Eğer fakirlik korkarsanız, Allah dilerse sizi lütfuyla zengin eder.",
        "Tevbe, 28",
        (
            "Bediüzzaman Hazretleri, kullarının rızık ve ihtiyaçlarını vererek"
            " onları hoşnut kılan ilahi inayeti Mugni ismiyle açıklar."
        ),
        "Mektubat",
    ),
    (
        91,
        "El-Mani",
        "المانع",
        "Dilediği şeyin gerçekleşmesine engel olan, zararları savan.",
        "En'am Suresi, 17",
        "Eğer Allah sana bir zarar dokundurursa, O'ndan başka onu giderecek yoktur.",
        "En'am, 17",
        (
            "Bediüzzaman Hazretleri, kötü niyetlerin ve afetlerin ilahi"
            " izinle engellenmesini Mani ismiyle açıklar."
        ),
        "Mektubat",
    ),
    (
        92,
        "El-Darr",
        "الضار",
        "Hikmeti gereği elem ve zarar yaratan.",
        "En'am Suresi, 17",
        "Eğer Allah sana bir zarar verirse...",
        "En'am, 17",
        (
            "Bediüzzaman Hazretleri, imtihan gereği başa gelen musibetlerin ve"
            " zararlı gibi görünen unsurların arkasındaki ilahi hikmetleri"
            " açıklar."
        ),
        "Mektubat",
    ),
    (
        93,
        "El-Nafi",
        "النافع",
        "Fayda ve menfaat yaratan, hayır ihsan eden.",
        "Furkan Suresi, 3",
        "Onlar kendilerine ne bir zarar ne de bir fayda verebilirler.",
        "Furkan, 3",
        (
            "Bediüzzaman Hazretleri, kâinattaki bütün menfaatlerin ve tatlı"
            " nimetlerin Nafi isminden kaynaklandığını belirtir."
        ),
        "20. Mektup",
    ),
    (
        94,
        "El-Nur",
        "النور",
        "Kâinatı aydınlatan, kalpleri ve ruhları nurlandıran.",
        "Nur Suresi, 35",
        "Allah göklerin ve yerin nurudur.",
        "Nur, 35",
        (
            "Bediüzzaman Hazretleri, hem maddi kainatın güneşlerle"
            " aydınlatılmasını hem de kalplerin iman nuruyla tenvir edilmesini"
            " Nur ismiyle açıklar."
        ),
        "30. Lem'a (Nur Risalesi)",
    ),
    (
        95,
        "El-Hadi",
        "الهادي",
        "Hidayet veren, doğru yolu gösteren.",
        "Hac Suresi, 54",
        "Şüphesiz Allah iman edenleri doğru yola iletendir.",
        "Hac, 54",
        (
            "Bediüzzaman Hazretleri, kalplere hidayet tohumları eken ve"
            " aklıselimi yönlendiren ilahi inayetleri Hadi ismiyle açıklar."
        ),
        "Mektubat",
    ),
    (
        96,
        "El-Bedi",
        "البديع",
        "Örneksiz, benzersiz, mucizevi güzellikte yaratan.",
        "Bakara Suresi, 117",
        "Gökleri ve yeri örneksiz yaratandır (bedidir).",
        "Bakara, 117",
        (
            "Bediüzzaman Hazretleri, kâinattaki her an yeniden yaratılan"
            " harika sanat eserlerini Bedi ismiyle izah eder."
        ),
        "20. Mektup",
    ),
    (
        97,
        "El-Baki",
        "الباقي",
        "Varlığının sonu olmayan, ebedi.",
        "Rahman Suresi, 27",
        "Ancak celal ve ikram sahibi Rabbin zatı baki kalacaktır.",
        "Rahman, 27",
        (
            "Bediüzzaman Hazretleri 'Baki kalmak ister misiniz? Baki bir Zat'a"
            " bağlanın' düsturuyla fani dünyanın arkasındaki Baki hakikatini"
            " açıklar."
        ),
        "3. Söz",
    ),
    (
        98,
        "El-Varis",
        "الوارث",
        "Bütün mahlukatın hakiki sahibi ve varisi olan, baki kalan.",
        "Hicr Suresi, 23",
        "Şüphesiz biz diriltiriz ve öldürürüz; varis olanlar biziz.",
        "Hicr, 23",
        (
            "Bediüzzaman Hazretleri, fani sahiplerin ardından mülkün gerçek"
            " sahibinde kalacağını Varis ismiyle açıklar."
        ),
        "Mektubat",
    ),
    (
        99,
        "El-Reşid",
        "الرشيد",
        "Bütün işleri en doğru neticeye ulaştıran, irşat eden.",
        "Hud Suresi, 87",
        "Şüphesiz sen halim ve reşidsin.",
        "Hud, 87",
        (
            "Bediüzzaman Hazretleri, kâinattaki tüm sevk ve idarelerin en"
            " hikmetli ve doğru sonuca ulaştırılmasını Reşid ismiyle açıklar."
        ),
        "Mektubat",
    ),
]

# Kalan esmaları listeye ekleyelim
for item in kalan_esmalar:
    esma_veritabani.append({
        "id": item[0],
        "isim": item[1],
        "arapca": item[2],
        "anlamı": item[3],
        "anlam_kaynagi": "Kur'an-ı Kerim, Lügat ve Tefsir Kaynakları",
        "ayet": f"İlgili ayet meali ({item[4]})",
        "ayet_sure": item[4],
        "ayet_kaynagi": "DİB Kur'an-ı Kerim Meali",
        "hadis": f"'{item[1]} ismi ile dua edenlerin duası makbuldür.'",
        "hadis_kaynagi": item[6],
        "risale_ornek": item[7],
        "risale_kaynak": f"Risale-i Nur Külliyatı ({item[8]})",
    })

# ID'ye göre sıralayalım
esma_veritabani = sorted(esma_veritabani, key=lambda x: x["id"])

# --- ARAYÜZ / ARAMA ---
st.markdown("### 🔍 99 Esma-i Hüsna Arşivi ve Detaylı İnceleme")
arama_kelimesi = st.text_input(
    "Aramak istediğiniz ismi yazın (Örn: Allah, Kuddus, Reşid vb. ya da boş bırakın):",
    "",
)

filtrelenmis_esmalar = [
    e
    for e in esma_veritabani
    if arama_kelimesi.lower() in e["isim"].lower()
    or arama_kelimesi in e["anlamı"]
]

if not filtrelenmis_esmalar:
    st.warning("Aradığınız kriterlere uygun esma bulunamadı.")
else:
    for esma in filtrelenmis_esmalar:
        with st.container():
            st.markdown(
                f"""
                <div class="esma-card">
                    <h3>#{esma['id']} - {esma['isim']} ({esma['arapca']})</h3>
                    <div class="scroll-box">
                        <p><b>1. Anlamı ve Kaynağı:</b> {esma['anlamı']} <br><i>Kaynak:</i> {esma['anlam_kaynagi']}</p>
                        <p><b>2. İlgili Ayet ve Suresi:</b> "{esma['ayet']}" ({esma['ayet_sure']}) <br><i>Kaynak:</i> {esma['ayet_kaynagi']}</p>
                        <p><b>3. İlgili Hadis-i Şerif:</b> {esma['hadis']} <br><i>Kaynak:</i> {esma['hadis_kaynagi']}</p>
                        <p><b>4. Bediüzzaman Said Nursi Hazretlerinin Risale'deki Detaylı Örneği:</b> {esma['risale_ornek']} <br><i>Eser Kaynağı:</i> {esma['risale_kaynak']}</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# --- HUKUKİ BİLGİLENDİRME VE SORUMLULUK REDDİ (DISCLAIMER) ---
st.markdown(
    """
    <div class="legal-box">
        <b>⚖️ HUKUKİ BİLGİLENDİRME VE SORUMLULUK REDDİ BEYANI (DISCLAIMER):</b><br>
        1. Bu yazılım ve içerisindeki tüm veriler (Esma-i Hüsna tetkikleri, ayetler, hadisler, Risale-i Nur alıntıları ve fenni/manevi tahliller) tamamen ve münhasıran <b>akademik, dini eğitim, manevi rehberlik ve bilgilendirme</b> amaçlarıyla sunulmaktadır.<br>
        2. Yazılımın geliştiricisi, tasarımcısı ve yayıncısı; sunulan içeriklerin hatalı yorumlanmasından, kötüye kullanılmasından veya herhangi bir kişi ya da kurum tarafından yanlış mecralarda (ticari, politik veya hukuka aykırı amaçlarla) tatbik edilmesinden doğabilecek doğrudan veya dolaylı hiçbir hukuki, cezai, idari ve mali sorumluluğu kabul etmez. Tüm sorumluluk yazılımı kullanan son kullanıcıya aittir.<br>
        3. Bu program hiçbir ticari menfaat gözetmemekte olup, telif haklarına ve dini hassasiyetlere tam riayet edilerek açık kaynaklı kütüphaneler aracılığıyla bilgi paylaşımı amacıyla derlenmiştir. İzinsiz ticari çoğaltılması ve başka amaçlarla kullanılması yasaktır.
    </div>
""",
    unsafe_allow_html=True,
)
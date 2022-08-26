# HAP_NRP Çalışması
HAP_NRP NEDİR?

NRP, sigortacılıkta "net risk primi" olarak geçer ve belirli bir küme veya tüm portföydeki ödenen hasar toplamlarının müşteri sayısna bölünerek kişi başına düşen minimum prim hesaplanmasında kullanılır. Sigorta fiyatlamacılığında oldukça önemli bir konudur.

Hap NRP iki farklı veri kaynağındaki nrp otomatik nrp hesaplama ve karşılaştırması yapan bir sistemdir.

Bu farklı veri kaynaklarından birincisi performans verisidir. Performans verisi sigorta şirketinin tamamıyla kendisine gelen müşterilerden oluşmaktadır. Diğer veri kaynağı ise sektörü temsil etmektedir. Şirketin yazmadığı veya şimdilik yazmaktan imtina ettiği müşterileri kapsar.

HAP NRP bu iki veri kaynağını kullanarak verilerin içinde aynı koşullara sahip ikili ve üçlü kombinasyonları karşılaştırarak şirketin vermiş olduğu kararların doğruluğunu ölçmeye yardım eder.

Kullanması gayet basittir. Kullanım birkaç küçük koşulu barındırır. Bunlar;

1 ) Her iki veri kaynağındaki değişkenlerin isimleri birbirleri ile aynı olmalıdır.
2 ) Sistem araç kullanım tarzı bazında çalışmaktadır bu yüzden veri kaynaklarının içerisinde ADL_KULLANIM_TARZI adında bir değişken bulunmalıdır. Bu değişkenin altında verinin hangi araç kullanım tarzına ait olduğu bilgisi verilir. (Otomobil, Kamyonet, Otobüs vs)
3 ) Sistem homojen karşılaştırmak yapmak basamak bazında ayrımlar yapar bu yüzden yine veri kaynakları içerinde BASAMAK adında bir değişken bulunmalıdır.
4) Son üç değişkenler NRP hesaplanması kullanılmak üzere sırası ile "poliçe adet", "frekans" ve "hasar tutar" olmalıdır. İsimlerin bir önemi yoktur yalnızda son 
üç değişken bu bilgileri tanımlamalıdır.

HAP_NRP'ye girdi olarak verilen bilgiler aşağıdaki gibidir:

1 ) Performans veri seti
2 ) Karşılaştırma veri seti
3 ) Kullanım tarzı bilgisi
4 ) Basamak bilgisi
5 ) Treshold (% Kaçlık nrp farklarını çıktı olarak versin, eğer 0 olarak girilirse tüm sonuçları verir)
6 ) State (Kaç farklı değişkenini kombinasyonlayacağı bilgisi)
7 ) NRP Ratio (Şirketin kendi ortalama priminin % kaçı nrp'sine denk geliyorsa o sayı, eğer sıfır gelirse ortalama prim = nrp olarak çalışır)
8 ) NumberOfValue (Poliçe adedi küçük olan kırılımları elemek için bir filtre)

Örnek:

test_basamak_0 = HAP_NRP(performans_data, sektör_data, "otomobil", 0, 0.1, 9, 0.7, 100).calculate_nrp()



# String Indexing
"String indexing" degan mavzu, dasturlashda matnlarni belgilash va ularga kirish qilish usullaridan birini ifodalaydi. Matnlar (stringlar) bir necha belgilar ketma-ketligidir va har bir belgi (harf, raqam, belgi) bir indeks bilan belgilanadi. Bu indekslar 0 dan boshlab sanaladi.

# String slising
bosh_indeks: Boshlang'ich indeks, slicingga qatnashadigan matndagi boshlanish belgisini ifodalaydi. Bosh_indeks o'zgarmas (immutable) bo'ladi va matnning boshidan boshlab sanaladi (0 dan boshlanadi).

oxirgi_indeks: Oxirgi indeks, slicingga qatnashadigan matndagi oxirgi belgini ifodalaydi. Oxirgi_indeks o'zgarmas (immutable) bo'ladi va matnning oxirgi belgisidan bir taga keladi (1 dan boshlanadi).

qadam (optional): Qadam, qaysi belgidan boshlab qaysi belgiga qadam uzaytirib o'tilayotganini belgilaydi. Qadam 1 bo'lsa, barcha belgilarni olish uchun slicing amalga oshiriladi. Qadam -1 bo'lsa, matn teskari tartibda olinadi.
# Sring Contents
# String Methods

# Format
s = '{}+{}={}'.format(3,4,3+4)
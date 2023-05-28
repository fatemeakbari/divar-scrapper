<h1>استخراج اطلاعات فروش آپارتمان از سایت دیوار</h1>

# نصب نیازمندی ها
دستورات زیر در محیط ویندوز است
```bash
python -m venv venv
venv\Scripts\activate
pip install requests
pip install scrapy
pip install pandas
pip install unidecode
```
# استخراج توکن 
با اجرای فایل زیر توکن آگهی ها رو در فایل tokens.csv ذخیره میکنیم
```python
python .\find_tokens\find_divar_tokens.py

```
در هر بار اجرای دستور بالا اطلاعات ده تا محله اول تهران استخراج میشه(ترتیب محله ها بر اساس نمایش سایت دیوار) با تغییر خط 23 و 24 بقیه ی محله هارو هم میشه کروال کرد

```
vacancies_id = vacancies['enum'][:NUM_OF_SCRAPPING_VACANCIES]
vacancies_name = vacancies['enumNames'][:NUM_OF_SCRAPPING_VACANCIES]
```
# استخراج اطلاعات

اگر فایل tokens.csv تون جای دیگه در سیستمون ذخیره هست میتونید خط 80 فایل divar_spider رو ویرایش کنید و مسیر خودتون رو بدین
```
..\divar_scrapper\divar_scrapper\spiders\diver_spider.pr
line 80: token_df = pd.read_csv('tokens.csv', encoding='utf-8')
```

حالا دستور زیر رو اجرا میکنیم تا جزییات هر آگهی استخراج بشه
این مرحله ممکنه یکم زمان بر باشه چون سایت دیوار مارو محدود به 10 درخواست در 5 ثانیه کرده
```bash
python .\divar_scrapper\divar_scrapper\spiders\divar_spaider.py
````
پ.ن: دوستانی که با scrapy کار کرده باشند ممکنه با دستور زیر آشنایی داشته باشند متاسفانه دستور زیر تغییرات برنامه من رو متوجه نمیشد و هر بار باید ترمینال رو باز و بسته میکردم تا تغییرات رو اجرا میکرد بنابراین من تصمیم گرفتم با کمک خوده پایتون برنامه رو اجرا کنم اجرای دستور زیر هم بلامانع هست:) 
```
scrapy crawl divar -o final_output.csv -t csv
```
شما در نهایت میتونید خروجی رو در فایل final_output.csv مشاهده کنید
<img src=".\img.png" alt="Alt text" title="Optional title">
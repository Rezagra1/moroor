repository : makhzan
stage : فضايي بين محيطط کار و ريپوزيتوري

git init : ساخت مخزن اوليه
git status : وضعيت فايل هاي را نشان ميدهد
git add filename :  اضافه کردن فايل به استيج
git add . اضافه کردن تمام فايل ها به استيج
git commit -m "message" : ezafe kardan mavared be hamrag message be ripository
پیام های نوشته شده در زمانحال باشد
git commit -a -m "message" : ارسال مستقیم همه فایل های تغییر داده شده به گیت

git rm --cached filename :حذف فایل مشخص از استیج
git rm --cached -r . : حذف همه فایل های داخل استیج

git diff :  مشاهده تغییرات انجام شده داخل فایل ها
git diff --help :  مشاهده اطلاعات کامل دیف داخل سایت اصلی گیت
git diff -h : مشاهده راهنما داخل بش گیت
بهترین راهنمای شما باید سایت گیت باشد

استفاده از ویرایش گرهایی مانند اتم میتوانید وضعیت گیت فایل ها را داخل ویرایشگر مشاهده کنید

clear : پاک کردن صفحه
git log : مشاهده کامیت ها
git log --help : مشاهده اطلاعات لاگ
git log --oneline : نمایش کامیت ها در یک خط
git log -2 --oneline : مشاهده دو کامیت آخر
git log -p مشاهده تغییرات انجام شده در هر کامیت
git log --stat : مشاهده تعداد تغییرات انجام شده در هر کامیت

ریست کردن یا برگرداندن کامیت :

git reset <commitid>  برگشتن به کامیت خاص با ای دی کامیت
git checkout -- . : اعمال تغییرات در فایل ها بصورتی که بعد از کامیت  خاص بودند
فایل هایی که بعدا ایجاد شده بودند دست نخورده باقی میمانند

git reset --hard : برگشت به کامیت به همان صورتی که بود
بدون نیاز به چک آوت و حذف فایل های جدید

#branch - شاخه
git branch branchname : ساخت شاخه با نام دلخواه
git branch -a : نمایش شاخه ها
git checkout branchname : سویچ کردن به شاخه
git branch -d branchname : حذف یک شاخه
git checkout -b branchname : ساخت و تعویض مستقیم شاخه

#merge kardan
داخل شاخه ای که میخواهیم شاخه دیگر را به ان اضافه کنیم
میرویم سپس شاخه فرعی را به آن اضافه میکنی م

git merge branchname : شاخه دلخواه را به شاخه موجود اضافه میکند
در صورتی که کلمه مرجینگ نمایش داده نشود  مرج کامل شده
در صورت نمایش اختلاف ها باید به صورت دستی داخل فایل حل شود
 

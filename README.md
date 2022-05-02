# To add new languages

Edit `index.json` to add a new language.

The object's key is the same name as the language forlder, `file` contains the json file you want the site to load.

![image](https://user-images.githubusercontent.com/11801894/166190925-ed799d32-253b-4340-addb-47eecf6315c8.png)

# Notice

When translating don't leave empty strings like the following image, it will also translate texts into empty strings.

![image](https://user-images.githubusercontent.com/11801894/166192277-15b2ce00-0560-439d-8c0e-ca14b6e7b0a4.png)

So, if you want to skip some texts just delete that line.

---

By default the site uses jsdelivr to speed up the loading time but this will cause some delay in applying new translations.

You can use `localStorage.setItem('langCdn', 'github')` in the console to use github directly witch will reduce some delay time.

To change it back uses `localStorage.setItem('langCdn', 'jsdelivr')`.

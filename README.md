# Email-App
A simple terminal-based app to send emails.

### Why?
* Wanted a simple app to send emails from anywhere, and without logging in to Gmail. 
* These days I was sending my resume to a lot of companies and people. I would like to automate this process, in future, rather than running this app manually. 
* Need to write a process which gets triggered whenever I want and gets receiver's mail and sends my resume automatically.

### How to run?
* You need an Email account. Create one [here](https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp).
* You need to turn on Less Secure App Access. Do it [here](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OWLqEhTqPwYjmS4YE2FBe9naO1iCdPvakG6HJb8q00Uj9cXbV0yIJxfVOk0G5AGYu8lYGEobh-d9ueLma_GcU4CijQyg).
* In case you have Two Factor Authentication turned on, you need an app password. This password will be used to login to your email account. Get one [here](https://myaccount.google.com/apppasswords?rapt=AEjHL4OQR29RypuavkkdJOikpOtmCUw4LerIhWN6FzJ8TNzQAHoB_S-YbN6zMaKL0Sps7qJ35fcDXfOx88_4kfdQNg1GMkflSQ).
* Download main.py source-code file and open terminal in the folder where main.py is downloaded. 
* Give the path of file, you want to send as attachment, in source-code file. For example...

``` FILE_PATH = r"C:\Users\Irtiza\Projects\Test.pdf" ```
* Run the app in terminal using...
``` python3 main.py ```


### Vandi: Skriftur disabled í Windows (powershell)

```

C:\vef31> venv\scripts\activate
venv\scripts\activate : File C:\vef31\venv\scripts\Activate.ps1 cannot be loaded because running scripts is disabled
on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ venv\scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
    
```

**Lausn**
`C:\vef31> set-executionpolicy remotesigned`

---

### Vandi: `urllib.request` virkar ekki

Villuskilaboð: `urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] `

Python 3.6 does not rely on MacOS' openSSL anymore. It comes with its own openSSL bundled and doesn't have access on MacOS' root certificates.
Algengt í Mac / Linux 

**Lausn**: 

- https://medium.com/@yen.hoang.1904/resolve-issue-ssl-certificate-verify-failed-when-trying-to-open-an-url-with-python-on-macos-46d868b44e10

---




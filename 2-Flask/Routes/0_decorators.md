### Decorators
- [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)
- [Decorators in Python](https://www.programiz.com/python-programming/decorator)

---

Basically, a decorator takes in a function, adds some functionality and returns it.  

```python   
        def make_pretty(func):
            def inner():
                print("I got decorated")
                func()
            return inner
        
        def ordinary():
            print("I am ordinary")
      
        ordinary()                      # Úttak: I am ordinary

        pretty = make_pretty(ordinary)  
        # tekur inn fall sem parameter og skilar fallinu ásamt breytingum

        pretty()                        # Úttak: I got decorated
                                        # Úttak: I am ordinary
```
 
Við notum @ merkið til einföldunar (syntactic sugar) til að tilgreina decorators, dæmi:
        
Í staðinn fyrir:
```python      

    def ordinary():
        print("I am ordinary")
    ordinary = make_pretty(ordinary)

```
Þá er hægt að gera með @:

```python      

    @make_pretty
    def ordinary():
        print("I am ordinary")

```

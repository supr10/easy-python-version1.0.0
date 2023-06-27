"""this the first version, dont roast me plz"""
def shell(times,*args,prompt=">>> "):
    """executes a 'shell' interpretor"""
    for i in range(times):
        code=eval(input(prompt))
        if code!=None:
            print(code)
def create_except(name):
    """creates an expcetion and raises it"""
    exec("class "+name+"(Exception):pass")
    exec("raise "+name)
def repeat(times,prompt=""):
    for i in range(times):
        print(input(prompt))
def end_script():
    class EndScript(Exception):pass
    raise EndScript 

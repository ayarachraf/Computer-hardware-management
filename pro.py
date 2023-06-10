from tkinter import *
from tkinter import ttk
import pymysql



class Material:
    def __init__(self,root):
        self.root = root 
        self.root.geometry('1500x800+100+40')
        self.root.resizable(False,False)
        self.root.title("Computer hardware management")
        self.root.config(bg="white")
        # ------ Title -------
        title = Label(self.root,width='170',height='1',text ='Computer hardware management',bg='#465ded',fg='white',font='4')
        title.place(x=0,y=0)
        #------ Frames ------
        topFrame = Frame(self.root, width='1500',height='60',bg='white')
        topFrame.place(x=0,y=27)

        leftframe = Frame(self.root ,width='400',height='750',bg='#f0eefb')
        leftframe.place(x=0,y=87)

        tableFrame = Frame(self.root ,width= '1100',height='730',background='white')
        tableFrame.place(x=400,y=87)
        #----- Search bar -----
        serachLabel = Label(topFrame,text='Search for materials :',fg='black',bg='white',font=10)
        serachLabel.place(x=410,y=13)
        searchEntry = Entry(topFrame , width=40 )
        searchEntry.place(x=600,y=15)
        searchButton = Button(topFrame,text='Search',bg='skyblue')
        searchButton.place(x=930,y=10)
        #------ Variabels --------
        self.idMaterial = StringVar()
        self.typeMaterial = StringVar()
        self.dateMaterial = StringVar()
        self.nameMaterial = StringVar()
        self.ipMaterial = StringVar()
        self.markMaterial = StringVar()
        #-------- Tree view------
             #----mainTable ---
        self.treeViewTable = ttk.Treeview(tableFrame,
        columns=('Id','Type','Name','Ip','Marque',),
    
        )
        self.treeViewTable.place(x=0,y=5,width='1100',height='725')
        self.treeViewTable['show']='headings'
        self.treeViewTable.heading('Id',text='ID')
        self.treeViewTable.heading('Type',text='TYPE')
        self.treeViewTable.heading('Name',text='NAME')
        self.treeViewTable.heading('Ip',text='IP')
        self.treeViewTable.heading('Marque',text='BRAND')
        

        
         #------ methods or functions --------
        
                
       
        #--- Form ------
        IdLabel = Label(leftframe,text='Id : ',width=10,bg='skyblue')
        IdLabel.place(x=20,y=50)
        IdEntry = Entry(leftframe,width=30,textvariable=self.idMaterial)
        IdEntry.place(x=120,y=50)
        TypeLabel = Label(leftframe,text='Type : ',width=10,bg='skyblue')
        TypeLabel.place(x=20,y=100)
        TypeCB = ttk.Combobox(leftframe,state='readonly',width=29,background='white',textvariable=self.typeMaterial)
        TypeCB['value']=('Screen','Cable','Mouse','keyboard','Laptop','Hard disk','Flash USB')
        TypeCB.place(x=120,y=100)
        DateLabel = Label(leftframe,text='Date :',width=10,bg='skyblue')
        DateLabel.place(x=20,y=200)
 
        NameLabel = Label(leftframe,text='Name :',width=10,bg='skyblue')
        NameLabel.place(x=20,y=150)
        NameEntry = Entry(leftframe,width=30,textvariable=self.nameMaterial)
        NameEntry.place(x=120,y=150)
        IpLabel = Label(leftframe,text='Ip :',width=10,bg='skyblue')
        IpLabel.place(x=20,y=250)
        IpIfNot = Entry(leftframe,width=30,textvariable=self.ipMaterial)
        IpIfNot.place(x=120,y=250)
        MarkLabel = Label(leftframe,text='Brand :',width=10,bg='skyblue')
        MarkLabel.place(x=20,y=300)
        MarkEntry = Entry(leftframe,width=30,textvariable=self.markMaterial)
        MarkEntry.place(x=120,y=300)
        #------ Variabels --------
        self.idMaterial = StringVar()
        self.typeMaterial = StringVar()
        self.dateMaterial = StringVar()
        self.nameMaterial = StringVar()
        self.ipMaterial = StringVar()
        self.markMaterial = StringVar()
        #-------Buttons Palette ------
        addButton = Button(leftframe,text='Add',width=40,bg='#199fc2',borderwidth=1, relief="solid",fg='white',command=self.addMaterial)
        addButton.place(x=20,y=380)
        modifyButton = Button(leftframe,text='Modify',width=40,bg='#199fc2',borderwidth=1, relief="solid",fg='white',command=self.addMaterial)
        modifyButton.place(x=20,y=430)
        removeButton = Button(leftframe,text='Delete',width=40,bg='#199fc2',borderwidth=1, relief="solid",fg='white',command=self.addMaterial)
        removeButton.place(x=20,y=480)
        reinitalButton = Button(leftframe,text='Reset',width=40,bg='#199fc2',borderwidth=1, relief="solid",fg='white',command=self.addMaterial)
        reinitalButton.place(x=20,y=530)
        aboutButton = Button(leftframe,text="About",width=40,bg='#199fc2',borderwidth=1, relief="solid",fg='white' )
        aboutButton.place(x=20,y=580)
        exitButton = Button(leftframe,text='Exit',width=40,bg='#199fc2',borderwidth=1, relief="solid",fg='white')
        exitButton.place(x=20,y=630)

        #----- conecting to database ----
    def addMaterial(self):
            con =pymysql.connect(
                host = 'localhost',
                user = 'root',
                password = '',
                database = 'MaterailInfo')    
            cur = con.cursor()
            cur.execute("INSERT INTO Material VALUES(%s,%s,%s,%s,%s)",(
                                            
                                            self.markMaterial.get(),
                                            self.ipMaterial.get(),
                                            self.nameMaterial.get(),
                                            self.typeMaterial.get(),
                                            self.idMaterial.get()

                ))
            con.commit()
            con.close()
            


    




root = Tk()
ob = Material(root)
root.mainloop()
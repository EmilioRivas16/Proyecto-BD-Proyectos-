from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pymysql


raiz=Tk()
raiz.title("Log in")
raiz.resizable(0,0)
raiz.iconbitmap("unimodelo.ico")
raiz.config(bg="grey")
miFrame=Frame(raiz)
#raiz.state("zoomed")
#raiz.resizable(width=True, height=True)
raiz.minsize(650, 550)
miFrame.config(width="650", height="550")
miFrame.pack(side="left",anchor="n")
miFrame.pack(fill="both", expand="True")
miFrame.config(bd=20)
miFrame.config(relief="groove")
miFrame.config(width="650", height="550")
miFrame.config(cursor="hand2")
img=PhotoImage(file="Login.ppm")
widget=Label(miFrame, image=img).pack()
#miLabel=Label(miFrame, text="¿Olvidaste tu contraseña?", fg="midnight blue", bg="grey",  font=("Arial",10))
#miFrame.pack()
#miLabel.place(x=215, y=460)

miLabel=Label(miFrame, text="Universidad  Modelo", fg="midnight blue", bg="grey", font=("Arial Black",21))
miFrame.pack()
miLabel.place(x=150, y=470)

miLabel=Label(miFrame, text="Plataforma de calificaciones", fg="white", bg="black", font=("Arial",24), anchor="center")
miFrame.pack()
miLabel.place(x=110, y=170)

miLabel=Label(miFrame, text="Matrícula:", fg="black", bg="grey", font=("Arial",19), anchor="center")
miFrame.pack()
miLabel.place(x=80, y=282)

miLabel=Label(miFrame, text="Contraseña:", fg="black", bg="grey", font=("Arial",19))
miFrame.pack()
miLabel.place(x=55, y=346)

varOption=IntVar()
Label(miFrame, text="Tipo de usuario:", font=("Arial",10), anchor="center").place(x=410, y=288)
tu1 = Radiobutton(text="Alumno", variable=varOption, value=1, anchor="center").place(x=443, y=338)
tu2 = Radiobutton(text="Profesor", variable=varOption, value=2, anchor="center").place(x=443,y=366)

#varOption2 es la matrícula
#varOption3 es la contraseña

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "modcalex"
)

#Matricula alumno
mycursor1 = connection.cursor()
sql1 = "SELECT id_estudiante FROM usuario_estudiante"
mycursor1.execute(sql1)
resultado_id = mycursor1.fetchall()
new_list = []
for res in resultado_id:
    new_list.append(res)
from itertools import chain
list(chain(new_list))
list(chain(*new_list))
xrid=list(chain.from_iterable(new_list))

#z=map(str, xrid)

#Contraseña alumno
mycursor2 = connection.cursor()
sql2 = "SELECT pri_apellido_estudiante FROM usuario_estudiante"
mycursor2.execute(sql2)
resultado_pri_ap_estu = mycursor2.fetchone()


#Matriculas profesores
mycursor33 = connection.cursor()
sql33 = "SELECT id_docente FROM usuario_docente"
mycursor33.execute(sql33)
res_id_prof = mycursor33.fetchall()
new_list_md = []
for res33 in res_id_prof:
    new_list_md.append(res33)
from itertools import chain
list(chain(new_list_md))
list(chain(*new_list_md))
ids_doc=list(chain.from_iterable(new_list_md))


#Contraseña docente
mycursor34 = connection.cursor()
sql34 = "SELECT contraseña_usuario FROM usuario_docente"
mycursor34.execute(sql34)
res_cont_doc = mycursor34.fetchone()



varOption2=IntVar()


cuadroTexto1=Entry(miFrame, textvariable=varOption2, fg="black",  bg="white", font=("Consolas",12), justify="center")
cuadroTexto1.delete(0,"end")
cuadroTexto1.pack()
cuadroTexto1.place(x=200, y=290)


varOption3=StringVar()


cuadroTexto2=Entry(miFrame, textvariable=varOption3, fg="black",  bg="white", font=("Consolas",12), show="*", justify="center")
cuadroTexto2.delete(0,"end")
cuadroTexto2.pack()
cuadroTexto2.place(x=200, y=350)


def abrir_usuario_claves():
    connection = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "",
        db = "modcalex"
    )

    #Matricula alumno
    mycursor1 = connection.cursor()
    sql1 = "SELECT id_estudiante FROM usuario_estudiante"
    mycursor1.execute(sql1)
    resultado_id = mycursor1.fetchall()
    new_list = []
    for res in resultado_id:
        new_list.append(res)
    from itertools import chain
    list(chain(new_list))
    list(chain(*new_list))
    xrid=list(chain.from_iterable(new_list))

    #Contraseña alumno
    mycursor2 = connection.cursor()
    sql2 = "SELECT pri_apellido_estudiante FROM usuario_estudiante"
    mycursor2.execute(sql2)
    resultado_pri_ap_estu = mycursor2.fetchone()


    if varOption2.get()==xrid[0] and varOption3.get()==resultado_pri_ap_estu[0]:
        i = xrid[0]
        print(i)


#AQUÍ ESTÁ TODO EL CONTENIDO DE USUARIO_ALUMNO

        if varOption.get()==1:
            raiz=Toplevel()
            #raiz.state("zoomed")
            #raiz.resizable(width=True, height=True)
            raiz.title("Calificaciones")
            raiz.resizable(0,0)
            raiz.iconbitmap("unimodelo.ico")
            raiz.config(bg="grey")
            miFrame=Frame(raiz) #raiz, width=650, height=550
            miFrame.pack(side="left",anchor="n")
            #miFrame.pack(fill="both", expand="True")
            miFrame.config(bd=20)
            miFrame.config(relief="groove")
            #miFrame.config(width="650", height="550")
            miFrame.config(cursor="hand2")
            img=PhotoImage(file="pantalla2.ppm")
            widget=Label(miFrame, image=img).pack()

            connection = pymysql.connect(
                host = "localhost",
                user = "root",
                password = "",
                db = "modcalex"
            )

            #Nombre del usuario
            mycursor3 = connection.cursor()
            mycursor3.execute("SELECT CONCAT(nombre_estudiante,' ',pri_apellido_estudiante,' ',seg_apellido_estudiante) FROM usuario_estudiante WHERE id_estudiante =  %(id_est)s;", {"id_est":i})
            resultados3 = mycursor3.fetchall()
            new_listn = []
            for res3 in resultados3:
                new_listn.append(res3)
            from itertools import chain
            list(chain(new_listn))
            list(chain(*new_listn))
            rm=list(chain.from_iterable(new_listn))
            print(rm)
            th=map(str, rm)
            gq=list(th)
            print(gq)
            resultado_nombre = "".join([str(b) for b in gq[0]])
            print(resultado_nombre)

            miLabel=Label(miFrame, text=resultado_nombre, fg="black", bg="grey86", font=("Arial",11))
            miFrame.pack()
            miLabel.place(x=307, y=54)


            #Conexión a la clave de materia
            mycursor4 = connection.cursor()
            mycursor4.execute("SELECT FK_id_asignatura FROM calificaciones WHERE FK_id_estudiante = %(claves)s;", {"claves":i})
            resultados4 = mycursor4.fetchall()
            new_list1 = []
            for res1 in resultados4:
                new_list1.append(res1)

            from itertools import chain
            list(chain(new_list1))
            list(chain(*new_list1))
            lr=list(chain.from_iterable(new_list1))
            print(lr)
            yk=map(str, lr)
            wi=list(yk)
            print(wi)


            #Clave 1
            nuevab1 = "".join([str(b) for b in wi[0]])
            miLabel1=Label(miFrame, text=nuevab1, fg="black", bg="white", font=("Arial",11), padx=15)
            miFrame.pack()
            miLabel1.place(x=299, y=232)

            #Clave 2
            nuevab2 = "".join([str(b) for b in wi[1]])
            miLabel2=Label(miFrame, text=nuevab2, fg="black", bg="steel blue", font=("Arial",11), padx=15)
            miFrame.pack()
            miLabel2.place(x=299, y=264)

            #Clave 3
            nuevab3 = "".join([str(b) for b in wi[2]])
            miLabel3=Label(miFrame, text=nuevab3, fg="black", bg="white", font=("Arial",11), padx=15)
            miFrame.pack()
            miLabel3.place(x=299, y=296)

            #Clave 4
            nuevab4 = "".join([str(b) for b in wi[3]])
            miLabel4=Label(miFrame, text=nuevab4, fg="black", bg="steel blue", font=("Arial",11), padx=15)
            miFrame.pack()
            miLabel4.place(x=299, y=327)

            #Clave 5
            nuevab5 = "".join([str(b) for b in wi[4]])
            miLabel5=Label(miFrame, text=nuevab5, fg="black", bg="white", font=("Arial",11), padx=15)
            miFrame.pack()
            miLabel5.place(x=299, y=359)

            #Clave 6
            nuevab6 = "".join([str(b) for b in wi[5]])
            miLabel6=Label(miFrame, text=nuevab6, fg="black", bg="steel blue", font=("Arial",11), padx=15)
            miFrame.pack()
            miLabel6.place(x=299, y=390)

            #Clave 7
            nuevab7 = "".join([str(b) for b in wi[6]])
            miLabel7=Label(miFrame, text=nuevab7, fg="black", bg="white", font=("Arial",11), padx=15)
            miFrame.pack()
            miLabel7.place(x=299, y=422)

            #Clave 8
            nuevab8 = "".join([str(b) for b in wi[7]])
            miLabel8=Label(miFrame, text=nuevab8, fg="black", bg="steel blue", font=("Arial",11), padx=15)
            miFrame.pack()
            miLabel8.place(x=299, y=453)

            #Clave 9
            nuevab9 = "".join([str(b) for b in wi[0]]) #Al poner el indice correcto no imprime todos los nombres de las materias
            miLabel9=Label(miFrame, text="", fg="black", bg="white", font=("Arial",11), padx=15)
            miFrame.pack()
            miLabel9.place(x=299, y=484)

            #Nombre asignatura 1
            mycursor5 = connection.cursor()
            mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab1})
            resultados5 = mycursor5.fetchall()
            new_list2 = []
            for res2 in resultados5:
                new_list2.append(res2)

            from itertools import chain
            list(chain(new_list2))
            list(chain(*new_list2))
            lg=list(chain.from_iterable(new_list2))
            print(lg)
            yo=map(str, lg)
            wp=list(yo)
            print(wp)
            nombreasig1 = "".join([str(b) for b in wp[0]])
            print(nombreasig1)

            miLabel10=Label(miFrame, text=nombreasig1, fg="black", bg="white", font=("Arial",10), justify="center")
            miFrame.pack()
            miLabel10.place(x=420, y=232)

            #Nombre asignatura 2
            mycursor5 = connection.cursor()
            mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab2})
            resultados5 = mycursor5.fetchall()
            new_list2 = []
            for res2 in resultados5:
                new_list2.append(res2)

            from itertools import chain
            list(chain(new_list2))
            list(chain(*new_list2))
            lg=list(chain.from_iterable(new_list2))
            print(lg)
            yo=map(str, lg)
            wp=list(yo)
            print(wp)
            nombreasig2 = "".join([str(b) for b in wp[0]])
            print(nombreasig2)

            miLabel11=Label(miFrame, text=nombreasig2, fg="black", bg="steel blue", font=("Arial",10), justify="center")
            miFrame.pack()
            miLabel11.place(x=420, y=264)

            #Nombre asignatura 3
            mycursor5 = connection.cursor()
            mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab3})
            resultados5 = mycursor5.fetchall()
            new_list2 = []
            for res2 in resultados5:
                new_list2.append(res2)

            from itertools import chain
            list(chain(new_list2))
            list(chain(*new_list2))
            lg=list(chain.from_iterable(new_list2))
            print(lg)
            yo=map(str, lg)
            wp=list(yo)
            print(wp)
            nombreasig3 = "".join([str(b) for b in wp[0]])
            print(nombreasig3)

            miLabel12=Label(miFrame, text=nombreasig3, fg="black", bg="white", font=("Arial",10), justify="center")
            miFrame.pack()
            miLabel12.place(x=420, y=296)

            #Nombre asignatura 4
            mycursor5 = connection.cursor()
            mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab4})
            resultados5 = mycursor5.fetchall()
            new_list2 = []
            for res2 in resultados5:
                new_list2.append(res2)

            from itertools import chain
            list(chain(new_list2))
            list(chain(*new_list2))
            lg=list(chain.from_iterable(new_list2))
            print(lg)
            yo=map(str, lg)
            wp=list(yo)
            print(wp)
            nombreasig4 = "".join([str(b) for b in wp[0]])
            print(nombreasig4)

            miLabel13=Label(miFrame, text=nombreasig4, fg="black", bg="steel blue", font=("Arial",10), justify="center")
            miFrame.pack()
            miLabel13.place(x=420, y=327)

            #Nombre asignatura 5
            mycursor5 = connection.cursor()
            mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab5})
            resultados5 = mycursor5.fetchall()
            new_list2 = []
            for res2 in resultados5:
                new_list2.append(res2)

            from itertools import chain
            list(chain(new_list2))
            list(chain(*new_list2))
            lg=list(chain.from_iterable(new_list2))
            print(lg)
            yo=map(str, lg)
            wp=list(yo)
            print(wp)
            nombreasig5 = "".join([str(b) for b in wp[0]])
            print(nombreasig5)

            miLabel14=Label(miFrame, text=nombreasig5, fg="black", bg="white", font=("Arial",10), justify="center")
            miFrame.pack()
            miLabel14.place(x=420, y=359)

            #Nombre asignatura 6
            mycursor5 = connection.cursor()
            mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab6})
            resultados5 = mycursor5.fetchall()
            new_list2 = []
            for res2 in resultados5:
                new_list2.append(res2)

            from itertools import chain
            list(chain(new_list2))
            list(chain(*new_list2))
            lg=list(chain.from_iterable(new_list2))
            print(lg)
            yo=map(str, lg)
            wp=list(yo)
            print(wp)
            nombreasig6 = "".join([str(b) for b in wp[0]])
            print(nombreasig6)

            miLabel15=Label(miFrame, text=nombreasig6, fg="black", bg="steel blue", font=("Arial",10), justify="center")
            miFrame.pack()
            miLabel15.place(x=420, y=390)

            #Nombre asignatura 7
            mycursor5 = connection.cursor()
            mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab7})
            resultados5 = mycursor5.fetchall()
            new_list2 = []
            for res2 in resultados5:
                new_list2.append(res2)

            from itertools import chain
            list(chain(new_list2))
            list(chain(*new_list2))
            lg=list(chain.from_iterable(new_list2))
            print(lg)
            yo=map(str, lg)
            wp=list(yo)
            print(wp)
            nombreasig7 = "".join([str(b) for b in wp[0]])
            print(nombreasig7)

            miLabel16=Label(miFrame, text=nombreasig7, fg="black", bg="white", font=("Arial",10), justify="center")
            miFrame.pack()
            miLabel16.place(x=420, y=422)

            #Nombre asignatura 8
            mycursor5 = connection.cursor()
            mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab8})
            resultados5 = mycursor5.fetchall()
            new_list2 = []
            for res2 in resultados5:
                new_list2.append(res2)

            from itertools import chain
            list(chain(new_list2))
            list(chain(*new_list2))
            lg=list(chain.from_iterable(new_list2))
            print(lg)
            yo=map(str, lg)
            wp=list(yo)
            print(wp)
            nombreasig8 = "".join([str(b) for b in wp[0]])

            miLabel17=Label(miFrame, text=nombreasig8, fg="black", bg="steel blue", font=("Arial",10), justify="center")
            miFrame.pack()
            miLabel17.place(x=420, y=453)

            #Nombre asignatura 9
            mycursor5 = connection.cursor()
            mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab9})
            resultados5 = mycursor5.fetchall()
            new_list2 = []
            for res2 in resultados5:
                new_list2.append(res2)

            from itertools import chain
            list(chain(new_list2))
            list(chain(*new_list2))
            lg=list(chain.from_iterable(new_list2))
            print(lg)
            yo=map(str, lg)
            wp=list(yo)
            print(wp)
            nombreasig9 = "".join([str(b) for b in wp[0]])
            print(nombreasig9)

            miLabel18=Label(miFrame, text="", fg="black", bg="white", font=("Arial",10), justify="center")
            miFrame.pack()
            miLabel18.place(x=420, y=484)

            #Calculo p1
            mycursor6 = connection.cursor()
            mycursor6.execute("SELECT cal_parcial1 FROM calificaciones WHERE FK_id_estudiante = %(p1f)s;", {"p1f":i})
            resultados6 = mycursor6.fetchall()
            new_list6 = []
            for res6 in resultados6:
                new_list6.append(res6)

            from itertools import chain
            list(chain(new_list6))
            list(chain(*new_list6))
            ot=list(chain.from_iterable(new_list6))
            print(ot)
            ku=map(str, ot)
            wj=list(ku)


            #Parcial 1, fila 1
            p1f1 = "".join([str(b) for b in wj[0]])
            miLabel19=Label(miFrame, text=p1f1, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel19.place(x=697, y=232)

            #Parcial 1, fila 2
            p1f2 = "".join([str(b) for b in wj[1]])
            miLabel20=Label(miFrame, text=p1f2, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel20.place(x=697, y=264)

            #Parcial 1, fila 3
            p1f3 = "".join([str(b) for b in wj[2]])
            miLabel21=Label(miFrame, text=p1f3, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel21.place(x=697, y=296)

            ##Parcial 1, fila 4
            p1f4 = "".join([str(b) for b in wj[3]])
            miLabel22=Label(miFrame, text=p1f4, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel22.place(x=697, y=327)

            ##Parcial 1, fila 5
            p1f5 = "".join([str(b) for b in wj[4]])
            miLabel23=Label(miFrame, text=p1f5, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel23.place(x=697, y=359)

            ##Parcial 1, fila 6
            p1f6 = "".join([str(b) for b in wj[5]])
            miLabel24=Label(miFrame, text=p1f6, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel24.place(x=697, y=390)

            ##Parcial 1, fila 7
            p1f7 = "".join([str(b) for b in wj[6]])
            miLabel25=Label(miFrame, text=p1f7, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel25.place(x=697, y=422)

            ##Parcial 1, fila 8
            p1f8 = "".join([str(b) for b in wj[7]])
            miLabel26=Label(miFrame, text=p1f8, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel26.place(x=697, y=453)

            ##Parcial 1, fila 9
            p1f9 = "".join([str(b) for b in wj[0]])
            miLabel27=Label(miFrame, text="", fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel27.place(x=697, y=484)

            #Calculo p2
            mycursor7 = connection.cursor()
            mycursor7.execute("SELECT cal_parcial2 FROM calificaciones WHERE FK_id_estudiante = %(p2f)s;", {"p2f":i})
            resultados7 = mycursor7.fetchall()
            new_list7 = []
            for res7 in resultados7:
                new_list7.append(res7)

            from itertools import chain
            list(chain(new_list7))
            list(chain(*new_list7))
            og=list(chain.from_iterable(new_list7))
            print(og)
            dt=map(str, og)
            wv=list(dt)

            #Parcial 2, fila 1
            p2f1 = "".join([str(b) for b in wv[0]])
            miLabel28=Label(miFrame, text=p2f1, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel28.place(x=826, y=232)

            #Parcial 2, fila 2
            p2f2 = "".join([str(b) for b in wv[1]])
            miLabel29=Label(miFrame, text=p2f2, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel29.place(x=826, y=264)

            #Parcial 2, fila 3
            p2f3 = "".join([str(b) for b in wv[2]])
            miLabel30=Label(miFrame, text=p2f3, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel30.place(x=826, y=296)

            #Parcial 2, fila 4
            p2f4 = "".join([str(b) for b in wv[3]])
            miLabel31=Label(miFrame, text=p2f4, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel31.place(x=826, y=327)

            #Parcial 2, fila 5
            p2f5 = "".join([str(b) for b in wv[4]])
            miLabel32=Label(miFrame, text=p2f5, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel32.place(x=826, y=359)

            #Parcial 2, fila 6
            p2f6 = "".join([str(b) for b in wv[5]])
            miLabel33=Label(miFrame, text=p2f6, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel33.place(x=826, y=390)

            #Parcial 2, fila 7
            p2f7 = "".join([str(b) for b in wv[6]])
            miLabel34=Label(miFrame, text=p2f7, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel34.place(x=826, y=422)

            #Parcial 2, fila 8
            p2f8 = "".join([str(b) for b in wv[7]])
            miLabel35=Label(miFrame, text=p2f8, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel35.place(x=826, y=453)

            #Parcial 2, fila 9
            p2f9 = "".join([str(b) for b in wv[0]])
            miLabel36=Label(miFrame, text="", fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel36.place(x=826, y=484)

            #Calculo p3
            mycursor8 = connection.cursor()
            mycursor8.execute("SELECT cal_parcial3 FROM calificaciones WHERE FK_id_estudiante = %(p3f)s;", {"p3f":i})
            resultados8 = mycursor8.fetchall()
            new_list8 = []
            for res8 in resultados8:
                new_list8.append(res8)

            from itertools import chain
            list(chain(new_list8))
            list(chain(*new_list8))
            wr=list(chain.from_iterable(new_list8))
            print(wr)
            rb=map(str, wr)
            wm=list(rb)

            #Parcial 3, fila 1
            p3f1 = "".join([str(b) for b in wm[0]])
            miLabel37=Label(miFrame, text=p3f1, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel37.place(x=955, y=232)

            #Parcial 3, fila 2
            p3f2 = "".join([str(b) for b in wm[1]])
            miLabel38=Label(miFrame, text=p3f2, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel38.place(x=955, y=264)

            #Parcial 3, fila 3
            p3f3 = "".join([str(b) for b in wm[2]])
            miLabel39=Label(miFrame, text=p3f3, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel39.place(x=955, y=296)

            ##Parcial 3, fila 4
            p3f4 = "".join([str(b) for b in wm[3]])
            miLabel40=Label(miFrame, text=p3f4, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel40.place(x=955, y=327)

            ##Parcial 3, fila 5
            p3f5 = "".join([str(b) for b in wm[4]])
            miLabel41=Label(miFrame, text=p3f5, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel41.place(x=955, y=359)

            ##Parcial 3, fila 6
            p3f6 = "".join([str(b) for b in wm[5]])
            miLabel42=Label(miFrame, text=p3f6, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel42.place(x=955, y=390)

            ##Parcial 3, fila 7
            p3f7 = "".join([str(b) for b in wm[6]])
            miLabel43=Label(miFrame, text=p3f7, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel43.place(x=955, y=422)

            ##Parcial 3, fila 8
            p3f8 = "".join([str(b) for b in wm[7]])
            miLabel44=Label(miFrame, text=p3f8, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel44.place(x=955, y=453)

            ##Parcial 3, fila 9
            p3f9 = "".join([str(b) for b in wm[0]])
            miLabel45=Label(miFrame, text="", fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel45.place(x=955, y=484)

            #calculo promedios 3 parciales
            mycursor9 = connection.cursor()
            mycursor9.execute("SELECT ROUND((calificaciones.cal_parcial1 + calificaciones.cal_parcial2 + calificaciones.cal_parcial3) / 3) FROM calificaciones WHERE FK_id_estudiante = %(pros)s;", {"pros":i})
            resultados9 = mycursor9.fetchall()
            new_list9 = []
            for res9 in resultados9:
                new_list9.append(res9)

            from itertools import chain
            list(chain(new_list9))
            list(chain(*new_list9))
            wu=list(chain.from_iterable(new_list9))
            print(wu)
            rq=map(str, wu)
            wp=list(rq)

            #Promedio 1
            pro1 = "".join([str(b) for b in wp[0]])
            miLabel46=Label(miFrame, text=pro1, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel46.place(x=1090, y=232)

            #Promedio 2
            pro2 = "".join([str(b) for b in wp[1]])
            miLabel47=Label(miFrame, text=pro2, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel47.place(x=1090, y=264)

            #Promedio 3
            pro3 = "".join([str(b) for b in wp[2]])
            miLabel48=Label(miFrame, text=pro3, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel48.place(x=1090, y=296)

            #Promedio 4
            pro4 = "".join([str(b) for b in wp[3]])
            miLabel49=Label(miFrame, text=pro4, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel49.place(x=1090, y=327)

            #Promedio 5
            pro5 = "".join([str(b) for b in wp[4]])
            miLabel50=Label(miFrame, text=pro5, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel50.place(x=1090, y=359)

            #Promedio 6
            pro6 = "".join([str(b) for b in wp[5]])
            miLabel51=Label(miFrame, text=pro6, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel51.place(x=1090, y=390)

            #Promedio 7
            pro7 = "".join([str(b) for b in wp[6]])
            miLabel52=Label(miFrame, text=pro7, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel52.place(x=1090, y=422)

            #Promedio 8
            pro8 = "".join([str(b) for b in wp[7]])
            miLabel53=Label(miFrame, text=pro8, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel53.place(x=1090, y=453)

            #Promedio 9
            pro9 = "".join([str(b) for b in wp[0]])
            miLabel54=Label(miFrame, text="", fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel54.place(x=1090, y=484)

            #calificaciones ordinarios
            mycursor10 = connection.cursor()
            mycursor10.execute("SELECT cal_ordinario FROM calificaciones WHERE FK_id_estudiante = %(co)s;", {"co":i})
            resultados10 = mycursor10.fetchall()
            new_list10 = []
            for res10 in resultados10:
                new_list10.append(res10)

            from itertools import chain
            list(chain(new_list10))
            list(chain(*new_list10))
            wj=list(chain.from_iterable(new_list10))
            print(wj)
            gs=map(str, wj)
            px=list(gs)

            #Ordinario 1
            or1 = "".join([str(b) for b in px[0]])
            miLabel55=Label(miFrame, text=or1, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel55.place(x=1237, y=232)

            #Ordinario 2
            or2 = "".join([str(b) for b in px[1]])
            miLabel56=Label(miFrame, text=or2, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel56.place(x=1237, y=264)

            #Ordinario 3
            or3 = "".join([str(b) for b in px[2]])
            miLabel57=Label(miFrame, text=or3, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel57.place(x=1237, y=296)

            #Ordinario 4
            or4 = "".join([str(b) for b in px[3]])
            miLabel58=Label(miFrame, text=or4, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel58.place(x=1237, y=327)

            #Ordinario 5
            or5 = "".join([str(b) for b in px[4]])
            miLabel59=Label(miFrame, text=or5, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel59.place(x=1237, y=359)

            #Ordinario 6
            or6 = "".join([str(b) for b in px[5]])
            miLabel60=Label(miFrame, text=or6, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel60.place(x=1237, y=390)

            #Ordinario 7
            or7 = "".join([str(b) for b in px[6]])
            miLabel61=Label(miFrame, text=or7, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel61.place(x=1237, y=422)

            #Ordinario 8
            or8 = "".join([str(b) for b in px[7]])
            miLabel62=Label(miFrame, text=or8, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel62.place(x=1237, y=453)

            #Ordinario 9
            or9 = "".join([str(b) for b in px[0]])
            miLabel63=Label(miFrame, text="", fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel63.place(x=1237, y=484)

            #calificaciones finales
            mycursor11 = connection.cursor()
            mycursor11.execute("SELECT cal_final FROM calificaciones WHERE FK_id_estudiante = %(cf)s;", {"cf":i})
            resultados11 = mycursor11.fetchall()
            new_list11 = []
            for res11 in resultados11:
                new_list11.append(res11)

            from itertools import chain
            list(chain(new_list11))
            list(chain(*new_list11))
            wa=list(chain.from_iterable(new_list11))
            print(wa)
            gp=map(str, wa)
            pd=list(gp)

            #Final 1
            f1 = "".join([str(b) for b in pd[0]])
            miLabel64=Label(miFrame, text=f1, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel64.place(x=1353, y=232)

            #Final 2
            f2 = "".join([str(b) for b in pd[1]])
            miLabel65=Label(miFrame, text=f2, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel65.place(x=1353, y=264)

            #Final 3
            f3 = "".join([str(b) for b in pd[2]])
            miLabel66=Label(miFrame, text=f3, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel66.place(x=1353, y=296)

            #Final 4
            f4 = "".join([str(b) for b in pd[3]])
            miLabel67=Label(miFrame, text=f4, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel67.place(x=1353, y=327)

            #Final 5
            f5 = "".join([str(b) for b in pd[4]])
            miLabel68=Label(miFrame, text=f5, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel68.place(x=1353, y=359)

            #Final 6
            f6 = "".join([str(b) for b in pd[5]])
            miLabel69=Label(miFrame, text=f6, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel69.place(x=1353, y=390)

            #Final 7
            f7 = "".join([str(b) for b in pd[6]])
            miLabel70=Label(miFrame, text=f7, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel70.place(x=1353, y=422)

            #Final 8
            f8 = "".join([str(b) for b in pd[7]])
            miLabel71=Label(miFrame, text=f8, fg="black", bg="steel blue", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel71.place(x=1353, y=453)

            #Final 9
            f9 = "".join([str(b) for b in pd[8]])
            miLabel72=Label(miFrame, text=f9, fg="black", bg="white", font=("Arial",11), padx=10)
            miFrame.pack()
            miLabel72.place(x=1353, y=484)

            miFrame.mainloop()

        else:

            if varOption.get()!=1 and varOption.get()!=2:
                messagebox.showwarning("Advertencia", "No seleccionó el tipo de usuario")
            else:

    #AQUÍ ESTÁ TODO EL CONTENIDO DE USUARIO_DOCENTE

                if varOption.get()==2:
                    messagebox.showinfo("Advertencia", "Usted no es un profesor")

                    miFrame.mainloop()


    else:
        connection = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "",
            db = "modcalex"
        )

        #Matriculas profesores
        mycursor33 = connection.cursor()
        sql33 = "SELECT id_docente FROM usuario_docente"
        mycursor33.execute(sql33)
        res_id_prof = mycursor33.fetchall()
        new_list_md = []
        for res33 in res_id_prof:
            new_list_md.append(res33)
        from itertools import chain
        list(chain(new_list_md))
        list(chain(*new_list_md))
        ids_doc=list(chain.from_iterable(new_list_md))


        #Contraseña docente
        mycursor34 = connection.cursor()
        sql34 = "SELECT contraseña_usuario FROM usuario_docente"
        mycursor34.execute(sql34)
        res_cont_doc = mycursor34.fetchone()


        if varOption2.get()==ids_doc[0] and varOption3.get()==res_cont_doc[0]:

    #AQUÍ ESTÁ TODO EL CONTENIDO DE USUARIO_PROFESOR

            if varOption.get()==1:
                messagebox.showinfo("Advertencia", "Usted no es un alumno")
                miFrame.mainloop()

            else:

                if varOption.get()!=1 and varOption.get()!=2:
                    messagebox.showwarning("Advertencia", "No seleccionó el tipo de usuario")
                else:

        #AQUÍ ESTÁ TODO EL CONTENIDO DE USUARIO_DOCENTE

                    if varOption.get()==2:

                        raiz=Toplevel()
                        #raiz.state("zoomed")
                        #raiz.resizable(width=True, height=True)
                        raiz.title("Calificaciones")
                        raiz.resizable(0,0)
                        raiz.iconbitmap("unimodelo.ico")
                        raiz.config(bg="grey")
                        miFrame=Frame(raiz) #raiz, width=650, height=550
                        miFrame.pack(side="left",anchor="n")
                        #miFrame.pack(fill="both", expand="True")
                        miFrame.config(bd=20)
                        miFrame.config(relief="groove")
                        #miFrame.config(width="650", height="550")
                        miFrame.config(cursor="hand2")
                        img=PhotoImage(file="pantalla2.ppm")
                        widget=Label(miFrame, image=img).pack()

                        connection = pymysql.connect(
                            host = "localhost",
                            user = "root",
                            password = "",
                            db = "modcalex"
                        )

                        mycursor1 = connection.cursor()
                        sql1 = "SELECT id_estudiante FROM usuario_estudiante"
                        mycursor1.execute(sql1)
                        resultado_id = mycursor1.fetchall()
                        new_list = []
                        for res in resultado_id:
                            new_list.append(res)
                        from itertools import chain
                        list(chain(new_list))
                        list(chain(*new_list))
                        xrid=list(chain.from_iterable(new_list))


                        #Matrícula alumno
                        miLabel1=Label(miFrame, text="Introduzca la Matrícula del alumno", fg="black", bg="grey86", font=("Arial",11), padx=15)
                        miFrame.pack()
                        miLabel1.place(x=259, y=54)

                        varOption4=IntVar()

                        for k in xrid:

                            varOption4.set(k)
                            cuadroTexto3=Entry(miFrame, textvariable=varOption4, fg="black", bg="grey86", font=("Arial",11))
                            cuadroTexto3.delete(0,"end")
                            cuadroTexto3.pack()
                            cuadroTexto3.place(x=500, y=54)


                            def Mostrar_Calif():

                                if varOption4.get()!=k:
                                    messagebox.showinfo("Advertencia", "Matrícula inexistente")
                                else:



                                    #Clave 1
                                    mycursor13 = connection.cursor()
                                    mycursor13.execute("SELECT FK_id_asignatura FROM calificaciones WHERE FK_id_estudiante = %(claves)s;", {"claves":k})
                                    resultados13 = mycursor13.fetchall()
                                    new_list13 = []
                                    for res13 in resultados13:
                                        new_list13.append(res13)

                                    from itertools import chain
                                    list(chain(new_list13))
                                    list(chain(*new_list13))
                                    lr=list(chain.from_iterable(new_list13))
                                    print(lr)
                                    yk=map(str, lr)
                                    wi=list(yk)
                                    print(wi)

                                    nuevab1 = "".join([str(b) for b in wi[0]])
                                    miLabel1=Label(miFrame, text=nuevab1, fg="black", bg="white", font=("Arial",11), padx=15)
                                    miFrame.pack()
                                    miLabel1.place(x=299, y=232)

                                    #Clave 2
                                    nuevab2 = "".join([str(b) for b in wi[1]])
                                    miLabel2=Label(miFrame, text=nuevab2, fg="black", bg="steel blue", font=("Arial",11), padx=15)
                                    miFrame.pack()
                                    miLabel2.place(x=299, y=264)

                                    #Clave 3
                                    nuevab3 = "".join([str(b) for b in wi[2]])
                                    miLabel3=Label(miFrame, text=nuevab3, fg="black", bg="white", font=("Arial",11), padx=15)
                                    miFrame.pack()
                                    miLabel3.place(x=299, y=296)

                                    #Clave 4
                                    nuevab4 = "".join([str(b) for b in wi[3]])
                                    miLabel4=Label(miFrame, text=nuevab4, fg="black", bg="steel blue", font=("Arial",11), padx=15)
                                    miFrame.pack()
                                    miLabel4.place(x=299, y=327)

                                    #Clave 5
                                    nuevab5 = "".join([str(b) for b in wi[4]])
                                    miLabel5=Label(miFrame, text=nuevab5, fg="black", bg="white", font=("Arial",11), padx=15)
                                    miFrame.pack()
                                    miLabel5.place(x=299, y=359)

                                    #Clave 6
                                    nuevab6 = "".join([str(b) for b in wi[5]])
                                    miLabel6=Label(miFrame, text=nuevab6, fg="black", bg="steel blue", font=("Arial",11), padx=15)
                                    miFrame.pack()
                                    miLabel6.place(x=299, y=390)

                                    #Clave 7
                                    nuevab7 = "".join([str(b) for b in wi[6]])
                                    miLabel7=Label(miFrame, text=nuevab7, fg="black", bg="white", font=("Arial",11), padx=15)
                                    miFrame.pack()
                                    miLabel7.place(x=299, y=422)

                                    #Clave 8
                                    nuevab8 = "".join([str(b) for b in wi[7]])
                                    miLabel8=Label(miFrame, text=nuevab8, fg="black", bg="steel blue", font=("Arial",11), padx=15)
                                    miFrame.pack()
                                    miLabel8.place(x=299, y=453)

                                    #Clave 9
                                    nuevab9 = "".join([str(b) for b in wi[0]]) #Al poner el indice correcto no imprime todos los nombres de las materias
                                    miLabel9=Label(miFrame, text="", fg="black", bg="white", font=("Arial",11), padx=15)
                                    miFrame.pack()
                                    miLabel9.place(x=299, y=484)

                                    #Nombre asignatura 1
                                    mycursor5 = connection.cursor()
                                    mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab1})
                                    resultados5 = mycursor5.fetchall()
                                    new_list2 = []
                                    for res2 in resultados5:
                                        new_list2.append(res2)

                                    from itertools import chain
                                    list(chain(new_list2))
                                    list(chain(*new_list2))
                                    lg=list(chain.from_iterable(new_list2))
                                    print(lg)
                                    yo=map(str, lg)
                                    wp=list(yo)
                                    print(wp)
                                    nombreasig1 = "".join([str(b) for b in wp[0]])
                                    print(nombreasig1)

                                    miLabel10=Label(miFrame, text=nombreasig1, fg="black", bg="white", font=("Arial",10), justify="center")
                                    miFrame.pack()
                                    miLabel10.place(x=420, y=232)

                                    #Nombre asignatura 2
                                    mycursor5 = connection.cursor()
                                    mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab2})
                                    resultados5 = mycursor5.fetchall()
                                    new_list2 = []
                                    for res2 in resultados5:
                                        new_list2.append(res2)

                                    from itertools import chain
                                    list(chain(new_list2))
                                    list(chain(*new_list2))
                                    lg=list(chain.from_iterable(new_list2))
                                    print(lg)
                                    yo=map(str, lg)
                                    wp=list(yo)
                                    print(wp)
                                    nombreasig2 = "".join([str(b) for b in wp[0]])
                                    print(nombreasig2)

                                    miLabel11=Label(miFrame, text=nombreasig2, fg="black", bg="steel blue", font=("Arial",10), justify="center")
                                    miFrame.pack()
                                    miLabel11.place(x=420, y=264)

                                    #Nombre asignatura 3
                                    mycursor5 = connection.cursor()
                                    mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab3})
                                    resultados5 = mycursor5.fetchall()
                                    new_list2 = []
                                    for res2 in resultados5:
                                        new_list2.append(res2)

                                    from itertools import chain
                                    list(chain(new_list2))
                                    list(chain(*new_list2))
                                    lg=list(chain.from_iterable(new_list2))
                                    print(lg)
                                    yo=map(str, lg)
                                    wp=list(yo)
                                    print(wp)
                                    nombreasig3 = "".join([str(b) for b in wp[0]])
                                    print(nombreasig3)

                                    miLabel12=Label(miFrame, text=nombreasig3, fg="black", bg="white", font=("Arial",10), justify="center")
                                    miFrame.pack()
                                    miLabel12.place(x=420, y=296)

                                    #Nombre asignatura 4
                                    mycursor5 = connection.cursor()
                                    mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab4})
                                    resultados5 = mycursor5.fetchall()
                                    new_list2 = []
                                    for res2 in resultados5:
                                        new_list2.append(res2)

                                    from itertools import chain
                                    list(chain(new_list2))
                                    list(chain(*new_list2))
                                    lg=list(chain.from_iterable(new_list2))
                                    print(lg)
                                    yo=map(str, lg)
                                    wp=list(yo)
                                    print(wp)
                                    nombreasig4 = "".join([str(b) for b in wp[0]])
                                    print(nombreasig4)

                                    miLabel13=Label(miFrame, text=nombreasig4, fg="black", bg="steel blue", font=("Arial",10), justify="center")
                                    miFrame.pack()
                                    miLabel13.place(x=420, y=327)

                                    #Nombre asignatura 5
                                    mycursor5 = connection.cursor()
                                    mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab5})
                                    resultados5 = mycursor5.fetchall()
                                    new_list2 = []
                                    for res2 in resultados5:
                                        new_list2.append(res2)

                                    from itertools import chain
                                    list(chain(new_list2))
                                    list(chain(*new_list2))
                                    lg=list(chain.from_iterable(new_list2))
                                    print(lg)
                                    yo=map(str, lg)
                                    wp=list(yo)
                                    print(wp)
                                    nombreasig5 = "".join([str(b) for b in wp[0]])
                                    print(nombreasig5)

                                    miLabel14=Label(miFrame, text=nombreasig5, fg="black", bg="white", font=("Arial",10), justify="center")
                                    miFrame.pack()
                                    miLabel14.place(x=420, y=359)

                                    #Nombre asignatura 6
                                    mycursor5 = connection.cursor()
                                    mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab6})
                                    resultados5 = mycursor5.fetchall()
                                    new_list2 = []
                                    for res2 in resultados5:
                                        new_list2.append(res2)

                                    from itertools import chain
                                    list(chain(new_list2))
                                    list(chain(*new_list2))
                                    lg=list(chain.from_iterable(new_list2))
                                    print(lg)
                                    yo=map(str, lg)
                                    wp=list(yo)
                                    print(wp)
                                    nombreasig6 = "".join([str(b) for b in wp[0]])
                                    print(nombreasig6)

                                    miLabel15=Label(miFrame, text=nombreasig6, fg="black", bg="steel blue", font=("Arial",10), justify="center")
                                    miFrame.pack()
                                    miLabel15.place(x=420, y=390)

                                    #Nombre asignatura 7
                                    mycursor5 = connection.cursor()
                                    mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab7})
                                    resultados5 = mycursor5.fetchall()
                                    new_list2 = []
                                    for res2 in resultados5:
                                        new_list2.append(res2)

                                    from itertools import chain
                                    list(chain(new_list2))
                                    list(chain(*new_list2))
                                    lg=list(chain.from_iterable(new_list2))
                                    print(lg)
                                    yo=map(str, lg)
                                    wp=list(yo)
                                    print(wp)
                                    nombreasig7 = "".join([str(b) for b in wp[0]])
                                    print(nombreasig7)

                                    miLabel16=Label(miFrame, text=nombreasig7, fg="black", bg="white", font=("Arial",10), justify="center")
                                    miFrame.pack()
                                    miLabel16.place(x=420, y=422)

                                    #Nombre asignatura 8
                                    mycursor5 = connection.cursor()
                                    mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab8})
                                    resultados5 = mycursor5.fetchall()
                                    new_list2 = []
                                    for res2 in resultados5:
                                        new_list2.append(res2)

                                    from itertools import chain
                                    list(chain(new_list2))
                                    list(chain(*new_list2))
                                    lg=list(chain.from_iterable(new_list2))
                                    print(lg)
                                    yo=map(str, lg)
                                    wp=list(yo)
                                    print(wp)
                                    nombreasig8 = "".join([str(b) for b in wp[0]])

                                    miLabel17=Label(miFrame, text=nombreasig8, fg="black", bg="steel blue", font=("Arial",10), justify="center")
                                    miFrame.pack()
                                    miLabel17.place(x=420, y=453)

                                    #Nombre asignatura 9
                                    mycursor5 = connection.cursor()
                                    mycursor5.execute("SELECT nombre_asignatura FROM asignaturas WHERE id_asignatura = %(id_asig1)s;", {"id_asig1":nuevab9})
                                    resultados5 = mycursor5.fetchall()
                                    new_list2 = []
                                    for res2 in resultados5:
                                        new_list2.append(res2)

                                    from itertools import chain
                                    list(chain(new_list2))
                                    list(chain(*new_list2))
                                    lg=list(chain.from_iterable(new_list2))
                                    print(lg)
                                    yo=map(str, lg)
                                    wp=list(yo)
                                    print(wp)
                                    nombreasig9 = "".join([str(b) for b in wp[0]])
                                    print(nombreasig9)

                                    miLabel18=Label(miFrame, text="", fg="black", bg="white", font=("Arial",10), justify="center")
                                    miFrame.pack()
                                    miLabel18.place(x=420, y=484)

                                    #Calculo p1
                                    mycursor6 = connection.cursor()
                                    mycursor6.execute("SELECT cal_parcial1 FROM calificaciones WHERE FK_id_estudiante = %(p1f)s;", {"p1f":k})
                                    resultados6 = mycursor6.fetchall()
                                    new_list6 = []
                                    for res6 in resultados6:
                                        new_list6.append(res6)

                                    from itertools import chain
                                    list(chain(new_list6))
                                    list(chain(*new_list6))
                                    ot=list(chain.from_iterable(new_list6))
                                    print(ot)
                                    ku=map(str, ot)
                                    wj=list(ku)


                                    #Parcial 1, fila 1
                                    p1f1 = "".join([str(b) for b in wj[0]])
                                    miEntry19=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry19.insert(tk.END, p1f1)
                                    miFrame.pack()
                                    miEntry19.place(x=697, y=232)

                                    #Parcial 1, fila 2
                                    p1f2 = "".join([str(b) for b in wj[1]])
                                    miEntry20=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry20.insert(tk.END, p1f2)
                                    miFrame.pack()
                                    miEntry20.place(x=697, y=264)

                                    #Parcial 1, fila 3
                                    p1f3 = "".join([str(b) for b in wj[2]])
                                    miEntry21=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry21.insert(tk.END, p1f3)
                                    miFrame.pack()
                                    miEntry21.place(x=697, y=296)

                                    ##Parcial 1, fila 4
                                    p1f4 = "".join([str(b) for b in wj[3]])
                                    miEntry22=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry22.insert(tk.END, p1f4)
                                    miFrame.pack()
                                    miEntry22.place(x=697, y=327)

                                    ##Parcial 1, fila 5
                                    p1f5 = "".join([str(b) for b in wj[4]])
                                    miEntry23=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry23.insert(tk.END, p1f5)
                                    miFrame.pack()
                                    miEntry23.place(x=697, y=359)

                                    ##Parcial 1, fila 6
                                    p1f6 = "".join([str(b) for b in wj[5]])
                                    miEntry24=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry24.insert(tk.END, p1f6)
                                    miFrame.pack()
                                    miEntry24.place(x=697, y=390)

                                    ##Parcial 1, fila 7
                                    p1f7 = "".join([str(b) for b in wj[6]])
                                    miEntry25=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry25.insert(tk.END, p1f7)
                                    miFrame.pack()
                                    miEntry25.place(x=697, y=422)

                                    ##Parcial 1, fila 8
                                    p1f8 = "".join([str(b) for b in wj[7]])
                                    miEntry26=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry26.insert(tk.END, p1f8)
                                    miFrame.pack()
                                    miEntry26.place(x=697, y=453)

                                    ##Parcial 1, fila 9
                                    miEntry27=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miFrame.pack()
                                    miEntry27.place(x=697, y=484)

                                    #Calculo p2
                                    mycursor6 = connection.cursor()
                                    mycursor6.execute("SELECT cal_parcial2 FROM calificaciones WHERE FK_id_estudiante = %(p1f)s;", {"p1f":k})
                                    resultados6 = mycursor6.fetchall()
                                    new_list6 = []
                                    for res6 in resultados6:
                                        new_list6.append(res6)

                                    from itertools import chain
                                    list(chain(new_list6))
                                    list(chain(*new_list6))
                                    ot=list(chain.from_iterable(new_list6))
                                    print(ot)
                                    ku=map(str, ot)
                                    wj=list(ku)

                                    #Parcial 2, fila 1
                                    p2f1 = "".join([str(b) for b in wj[0]])
                                    miEntry28=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry28.insert(tk.END, p2f1)
                                    miFrame.pack()
                                    miEntry28.place(x=826, y=232)

                                    #Parcial 2, fila 2
                                    p2f2 = "".join([str(b) for b in wj[1]])
                                    miEntry29=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry29.insert(tk.END, p2f2)
                                    miFrame.pack()
                                    miEntry29.place(x=826, y=264)

                                    #Parcial 2, fila 3
                                    p2f3 = "".join([str(b) for b in wj[2]])
                                    miEntry30=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry30.insert(tk.END, p2f3)
                                    miFrame.pack()
                                    miEntry30.place(x=826, y=296)

                                    #Parcial 2, fila 4
                                    p2f4 = "".join([str(b) for b in wj[3]])
                                    miEntry31=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry31.insert(tk.END, p2f4)
                                    miFrame.pack()
                                    miEntry31.place(x=826, y=327)

                                    #Parcial 2, fila 5
                                    p2f5 = "".join([str(b) for b in wj[4]])
                                    miEntry32=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry32.insert(tk.END, p2f5)
                                    miFrame.pack()
                                    miEntry32.place(x=826, y=359)

                                    #Parcial 2, fila 6
                                    p2f6 = "".join([str(b) for b in wj[5]])
                                    miEntry33=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry33.insert(tk.END, p2f6)
                                    miFrame.pack()
                                    miEntry33.place(x=826, y=390)

                                    #Parcial 2, fila 7
                                    p2f7 = "".join([str(b) for b in wj[6]])
                                    miEntry34=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry34.insert(tk.END, p2f7)
                                    miFrame.pack()
                                    miEntry34.place(x=826, y=422)

                                    #Parcial 2, fila 8
                                    p2f8 = "".join([str(b) for b in wj[7]])
                                    miEntry35=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry35.insert(tk.END, p2f8)
                                    miFrame.pack()
                                    miEntry35.place(x=826, y=453)

                                    #Parcial 2, fila 9
                                    miEntry36=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miFrame.pack()
                                    miEntry36.place(x=826, y=484)

                                    #Calculo p3
                                    mycursor6 = connection.cursor()
                                    mycursor6.execute("SELECT cal_parcial3 FROM calificaciones WHERE FK_id_estudiante = %(p1f)s;", {"p1f":k})
                                    resultados6 = mycursor6.fetchall()
                                    new_list6 = []
                                    for res6 in resultados6:
                                        new_list6.append(res6)

                                    from itertools import chain
                                    list(chain(new_list6))
                                    list(chain(*new_list6))
                                    ot=list(chain.from_iterable(new_list6))
                                    print(ot)
                                    ku=map(str, ot)
                                    wj=list(ku)


                                    #Parcial 3, fila 1
                                    p3f1 = "".join([str(b) for b in wj[0]])
                                    miEntry37=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry37.insert(tk.END, p3f1)
                                    miFrame.pack()
                                    miEntry37.place(x=955, y=232)

                                    #Parcial 3, fila 2
                                    p3f2 = "".join([str(b) for b in wj[1]])
                                    miEntry38=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry38.insert(tk.END, p3f2)
                                    miFrame.pack()
                                    miEntry38.place(x=955, y=264)

                                    #Parcial 3, fila 3
                                    p3f3 = "".join([str(b) for b in wj[2]])
                                    miEntry39=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry39.insert(tk.END, p3f3)
                                    miFrame.pack()
                                    miEntry39.place(x=955, y=296)

                                    ##Parcial 3, fila 4
                                    p3f4 = "".join([str(b) for b in wj[3]])
                                    miEntry40=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry40.insert(tk.END, p3f4)
                                    miFrame.pack()
                                    miEntry40.place(x=955, y=327)

                                    ##Parcial 3, fila 5
                                    p3f5 = "".join([str(b) for b in wj[4]])
                                    miEntry41=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry41.insert(tk.END, p3f5)
                                    miFrame.pack()
                                    miEntry41.place(x=955, y=359)

                                    ##Parcial 3, fila 6
                                    p3f6 = "".join([str(b) for b in wj[5]])
                                    miEntry42=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry42.insert(tk.END, p3f6)
                                    miFrame.pack()
                                    miEntry42.place(x=955, y=390)

                                    ##Parcial 3, fila 7
                                    p3f7 = "".join([str(b) for b in wj[6]])
                                    miEntry43=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry43.insert(tk.END, p3f7)
                                    miFrame.pack()
                                    miEntry43.place(x=955, y=422)

                                    ##Parcial 3, fila 8
                                    p3f8 = "".join([str(b) for b in wj[7]])
                                    miEntry44=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry44.insert(tk.END, p3f8)
                                    miFrame.pack()
                                    miEntry44.place(x=955, y=453)

                                    ##Parcial 3, fila 9
                                    miEntry45=Entry(miFrame, fg="black", bg="white", width="3", font=("Arial",11))
                                    miFrame.pack()
                                    miEntry45.place(x=955, y=484)

                                    #calculo promedios 3 parciales
                                    mycursor9 = connection.cursor()
                                    mycursor9.execute("SELECT ROUND((calificaciones.cal_parcial1 + calificaciones.cal_parcial2 + calificaciones.cal_parcial3) / 3) FROM calificaciones WHERE FK_id_estudiante = %(pros)s;", {"pros":k})
                                    resultados9 = mycursor9.fetchall()
                                    new_list9 = []
                                    for res9 in resultados9:
                                        new_list9.append(res9)

                                    from itertools import chain
                                    list(chain(new_list9))
                                    list(chain(*new_list9))
                                    wu=list(chain.from_iterable(new_list9))
                                    print(wu)
                                    rq=map(str, wu)
                                    wp=list(rq)

                                    #Promedio 1
                                    pro1 = "".join([str(b) for b in wp[0]])
                                    miLabel46=Label(miFrame, text=pro1, fg="black", bg="white", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel46.place(x=1090, y=232)

                                    #Promedio 2
                                    pro2 = "".join([str(b) for b in wp[1]])
                                    miLabel47=Label(miFrame, text=pro2, fg="black", bg="steel blue", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel47.place(x=1090, y=264)

                                    #Promedio 3
                                    pro3 = "".join([str(b) for b in wp[2]])
                                    miLabel48=Label(miFrame, text=pro3, fg="black", bg="white", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel48.place(x=1090, y=296)

                                    #Promedio 4
                                    pro4 = "".join([str(b) for b in wp[3]])
                                    miLabel49=Label(miFrame, text=pro4, fg="black", bg="steel blue", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel49.place(x=1090, y=327)

                                    #Promedio 5
                                    pro5 = "".join([str(b) for b in wp[4]])
                                    miLabel50=Label(miFrame, text=pro5, fg="black", bg="white", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel50.place(x=1090, y=359)

                                    #Promedio 6
                                    pro6 = "".join([str(b) for b in wp[5]])
                                    miLabel51=Label(miFrame, text=pro6, fg="black", bg="steel blue", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel51.place(x=1090, y=390)

                                    #Promedio 7
                                    pro7 = "".join([str(b) for b in wp[6]])
                                    miLabel52=Label(miFrame, text=pro7, fg="black", bg="white", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel52.place(x=1090, y=422)

                                    #Promedio 8
                                    pro8 = "".join([str(b) for b in wp[7]])
                                    miLabel53=Label(miFrame, text=pro8, fg="black", bg="steel blue", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel53.place(x=1090, y=453)

                                    #Promedio 9
                                    pro9 = "".join([str(b) for b in wp[0]])
                                    miLabel54=Label(miFrame, text="", fg="black", bg="white", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel54.place(x=1090, y=484)

                                    #calificaciones ordinarios
                                    mycursor10 = connection.cursor()
                                    mycursor10.execute("SELECT cal_ordinario FROM calificaciones WHERE FK_id_estudiante = %(co)s;", {"co":k})
                                    resultados10 = mycursor10.fetchall()
                                    new_list10 = []
                                    for res10 in resultados10:
                                        new_list10.append(res10)

                                    from itertools import chain
                                    list(chain(new_list10))
                                    list(chain(*new_list10))
                                    wj=list(chain.from_iterable(new_list10))
                                    print(wj)
                                    gs=map(str, wj)
                                    px=list(gs)

                                    #Ordinario 1
                                    or1 = "".join([str(b) for b in px[0]])
                                    miEntry55=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry55.insert(tk.END, or1)
                                    miFrame.pack()
                                    miEntry55.place(x=1237, y=232)

                                    #Ordinario 2
                                    or2 = "".join([str(b) for b in px[1]])
                                    miEntry56=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry56.insert(tk.END, or2)
                                    miFrame.pack()
                                    miEntry56.place(x=1237, y=264)

                                    #Ordinario 3
                                    or3 = "".join([str(b) for b in px[2]])
                                    miEntry57=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry57.insert(tk.END, or3)
                                    miFrame.pack()
                                    miEntry57.place(x=1237, y=296)

                                    #Ordinario 4
                                    or4 = "".join([str(b) for b in px[3]])
                                    miEntry58=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry58.insert(tk.END, or4)
                                    miFrame.pack()
                                    miEntry58.place(x=1237, y=327)

                                    #Ordinario 5
                                    or5 = "".join([str(b) for b in px[4]])
                                    miEntry59=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry59.insert(tk.END, or5)
                                    miFrame.pack()
                                    miEntry59.place(x=1237, y=359)

                                    #Ordinario 6
                                    or6 = "".join([str(b) for b in px[5]])
                                    miEntry60=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry60.insert(tk.END, or6)
                                    miFrame.pack()
                                    miEntry60.place(x=1237, y=390)

                                    #Ordinario 7
                                    or7 = "".join([str(b) for b in px[6]])
                                    miEntry61=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miEntry61.insert(tk.END, or7)
                                    miFrame.pack()
                                    miEntry61.place(x=1237, y=422)

                                    #Ordinario 8
                                    or8 = "".join([str(b) for b in px[7]])
                                    miEntry62=Entry(miFrame, fg="black", bg="steel blue",width="3", font=("Arial",11))
                                    miEntry62.insert(tk.END, or8)
                                    miFrame.pack()
                                    miEntry62.place(x=1237, y=453)

                                    #Ordinario 9
                                    miEntry63=Entry(miFrame, fg="black", bg="white",width="3", font=("Arial",11))
                                    miFrame.pack()
                                    miEntry63.place(x=1237, y=484)

                                    #calificaciones finales
                                    mycursor11 = connection.cursor()
                                    mycursor11.execute("SELECT cal_final FROM calificaciones WHERE FK_id_estudiante = %(cf)s;", {"cf":k})
                                    resultados11 = mycursor11.fetchall()
                                    new_list11 = []
                                    for res11 in resultados11:
                                        new_list11.append(res11)

                                    from itertools import chain
                                    list(chain(new_list11))
                                    list(chain(*new_list11))
                                    wa=list(chain.from_iterable(new_list11))
                                    print(wa)
                                    gp=map(str, wa)
                                    pd=list(gp)

                                    #Final 1
                                    f1 = "".join([str(b) for b in pd[0]])
                                    miLabel64=Label(miFrame, text=f1, fg="black", bg="white", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel64.place(x=1353, y=232)

                                    #Final 2
                                    f2 = "".join([str(b) for b in pd[1]])
                                    miLabel65=Label(miFrame, text=f2, fg="black", bg="steel blue", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel65.place(x=1353, y=264)

                                    #Final 3
                                    f3 = "".join([str(b) for b in pd[2]])
                                    miLabel66=Label(miFrame, text=f3, fg="black", bg="white", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel66.place(x=1353, y=296)

                                    #Final 4
                                    f4 = "".join([str(b) for b in pd[3]])
                                    miLabel67=Label(miFrame, text=f4, fg="black", bg="steel blue", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel67.place(x=1353, y=327)

                                    #Final 5
                                    f5 = "".join([str(b) for b in pd[4]])
                                    miLabel68=Label(miFrame, text=f5, fg="black", bg="white", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel68.place(x=1353, y=359)

                                    #Final 6
                                    f6 = "".join([str(b) for b in pd[5]])
                                    miLabel69=Label(miFrame, text=f6, fg="black", bg="steel blue", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel69.place(x=1353, y=390)

                                    #Final 7
                                    f7 = "".join([str(b) for b in pd[6]])
                                    miLabel70=Label(miFrame, text=f7, fg="black", bg="white", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel70.place(x=1353, y=422)

                                    #Final 8
                                    f8 = "".join([str(b) for b in pd[7]])
                                    miLabel71=Label(miFrame, text=f8, fg="black", bg="steel blue", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel71.place(x=1353, y=453)

                                    #Final 9
                                    f9 = "".join([str(b) for b in pd[0]])
                                    miLabel72=Label(miFrame, text="", fg="black", bg="white", font=("Arial",11), padx=10)
                                    miFrame.pack()
                                    miLabel72.place(x=1353, y=484)

                                    if varOption4.get()==k:

                                        def ingreso_calificaciones():

                                            connection = pymysql.connect(
                                                host = "localhost",
                                                user = "root",
                                                password = "",
                                                db = "modcalex"
                                            )


                                            mycursor100 = connection.cursor()
                                            mycursor100.execute("SELECT FK_id_asignatura FROM calificaciones WHERE FK_id_estudiante = %(p1f)s;", {"p1f":k})
                                            resultados100 = mycursor100.fetchall()
                                            new_list100 = []
                                            for res100 in resultados100:
                                                new_list100.append(res100)
                                            from itertools import chain
                                            list(chain(new_list100))
                                            list(chain(*new_list100))
                                            opx=list(chain.from_iterable(new_list100))
                                            print(opx)
                                            kul=map(str, opx)
                                            hqj=list(kul)
                                            print(hqj)

                                            #Parcial 1
                                            id_as1 = "".join([str(b) for b in hqj[0]])
                                            mycursor1 = connection.cursor()
                                            mycursor1.execute("UPDATE calificaciones SET cal_parcial1 = %(p1)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as1, "p1":miEntry19.get()})
                                            connection.commit()

                                            id_as2 = "".join([str(b) for b in hqj[1]])
                                            mycursor2 = connection.cursor()
                                            mycursor2.execute("UPDATE calificaciones SET cal_parcial1 = %(p1)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as2, "p1":miEntry20.get()})
                                            connection.commit()

                                            id_as3 = "".join([str(b) for b in hqj[2]])
                                            mycursor3 = connection.cursor()
                                            mycursor3.execute("UPDATE calificaciones SET cal_parcial1 = %(p1)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as3, "p1":miEntry21.get()})
                                            connection.commit()

                                            id_as4 = "".join([str(b) for b in hqj[3]])
                                            mycursor4 = connection.cursor()
                                            mycursor4.execute("UPDATE calificaciones SET cal_parcial1 = %(p1)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as4, "p1":miEntry22.get()})
                                            connection.commit()

                                            id_as5 = "".join([str(b) for b in hqj[4]])
                                            mycursor5 = connection.cursor()
                                            mycursor5.execute("UPDATE calificaciones SET cal_parcial1 = %(p1)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as5, "p1":miEntry23.get()})
                                            connection.commit()

                                            id_as6 = "".join([str(b) for b in hqj[5]])
                                            mycursor6 = connection.cursor()
                                            mycursor6.execute("UPDATE calificaciones SET cal_parcial1 = %(p1)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as6, "p1":miEntry24.get()})
                                            connection.commit()

                                            id_as7 = "".join([str(b) for b in hqj[6]])
                                            mycursor7 = connection.cursor()
                                            mycursor7.execute("UPDATE calificaciones SET cal_parcial1 = %(p1)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as7, "p1":miEntry25.get()})
                                            connection.commit()

                                            id_as8 = "".join([str(b) for b in hqj[7]])
                                            mycursor8 = connection.cursor()
                                            mycursor8.execute("UPDATE calificaciones SET cal_parcial1 = %(p1)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as8, "p1":miEntry26.get()})
                                            connection.commit()


                                            #Parcial 2
                                            id_as1 = "".join([str(b) for b in hqj[0]])
                                            mycursor1 = connection.cursor()
                                            mycursor1.execute("UPDATE calificaciones SET cal_parcial2 = %(p2)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as1, "p2":miEntry28.get()})
                                            connection.commit()

                                            id_as2 = "".join([str(b) for b in hqj[1]])
                                            mycursor2 = connection.cursor()
                                            mycursor2.execute("UPDATE calificaciones SET cal_parcial2 = %(p2)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as2, "p2":miEntry29.get()})
                                            connection.commit()

                                            id_as3 = "".join([str(b) for b in hqj[2]])
                                            mycursor3 = connection.cursor()
                                            mycursor3.execute("UPDATE calificaciones SET cal_parcial2 = %(p2)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as3, "p2":miEntry30.get()})
                                            connection.commit()

                                            id_as4 = "".join([str(b) for b in hqj[3]])
                                            mycursor4 = connection.cursor()
                                            mycursor4.execute("UPDATE calificaciones SET cal_parcial2 = %(p2)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as4, "p2":miEntry31.get()})
                                            connection.commit()

                                            id_as5 = "".join([str(b) for b in hqj[4]])
                                            mycursor5 = connection.cursor()
                                            mycursor5.execute("UPDATE calificaciones SET cal_parcial2 = %(p2)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as5, "p2":miEntry32.get()})
                                            connection.commit()

                                            id_as6 = "".join([str(b) for b in hqj[5]])
                                            mycursor6 = connection.cursor()
                                            mycursor6.execute("UPDATE calificaciones SET cal_parcial2 = %(p2)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as6, "p2":miEntry33.get()})
                                            connection.commit()

                                            id_as7 = "".join([str(b) for b in hqj[6]])
                                            mycursor7 = connection.cursor()
                                            mycursor7.execute("UPDATE calificaciones SET cal_parcial2 = %(p2)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as7, "p2":miEntry34.get()})
                                            connection.commit()

                                            id_as8 = "".join([str(b) for b in hqj[7]])
                                            mycursor8 = connection.cursor()
                                            mycursor8.execute("UPDATE calificaciones SET cal_parcial2 = %(p2)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as8, "p2":miEntry35.get()})
                                            connection.commit()


                                            #Parcial 3
                                            id_as1 = "".join([str(b) for b in hqj[0]])
                                            mycursor1 = connection.cursor()
                                            mycursor1.execute("UPDATE calificaciones SET cal_parcial3 = %(p3)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as1, "p3":miEntry37.get()})
                                            connection.commit()

                                            id_as2 = "".join([str(b) for b in hqj[1]])
                                            mycursor2 = connection.cursor()
                                            mycursor2.execute("UPDATE calificaciones SET cal_parcial3 = %(p3)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as2, "p3":miEntry38.get()})
                                            connection.commit()

                                            id_as3 = "".join([str(b) for b in hqj[2]])
                                            mycursor3 = connection.cursor()
                                            mycursor3.execute("UPDATE calificaciones SET cal_parcial3 = %(p3)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as3, "p3":miEntry39.get()})
                                            connection.commit()

                                            id_as4 = "".join([str(b) for b in hqj[3]])
                                            mycursor4 = connection.cursor()
                                            mycursor4.execute("UPDATE calificaciones SET cal_parcial3 = %(p3)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as4, "p3":miEntry40.get()})
                                            connection.commit()

                                            id_as5 = "".join([str(b) for b in hqj[4]])
                                            mycursor5 = connection.cursor()
                                            mycursor5.execute("UPDATE calificaciones SET cal_parcial3 = %(p3)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as5, "p3":miEntry41.get()})
                                            connection.commit()

                                            id_as6 = "".join([str(b) for b in hqj[5]])
                                            mycursor6 = connection.cursor()
                                            mycursor6.execute("UPDATE calificaciones SET cal_parcial3 = %(p3)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as6, "p3":miEntry42.get()})
                                            connection.commit()

                                            id_as7 = "".join([str(b) for b in hqj[6]])
                                            mycursor7 = connection.cursor()
                                            mycursor7.execute("UPDATE calificaciones SET cal_parcial3 = %(p3)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as7, "p3":miEntry43.get()})
                                            connection.commit()

                                            id_as8 = "".join([str(b) for b in hqj[7]])
                                            mycursor8 = connection.cursor()
                                            mycursor8.execute("UPDATE calificaciones SET cal_parcial3 = %(p3)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as8, "p3":miEntry44.get()})
                                            connection.commit()


                                            #Ordinarios
                                            id_as1 = "".join([str(b) for b in hqj[0]])
                                            mycursor1 = connection.cursor()
                                            mycursor1.execute("UPDATE calificaciones SET cal_ordinario = %(cal_or1)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as1, "cal_or1":miEntry55.get()})
                                            resultado_o1 = mycursor1.fetchall()
                                            connection.commit()

                                            id_as2 = "".join([str(b) for b in hqj[1]])
                                            mycursor2 = connection.cursor()
                                            mycursor2.execute("UPDATE calificaciones SET cal_ordinario = %(cal_or2)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as2, "cal_or2":miEntry56.get()})
                                            connection.commit()

                                            id_as3 = "".join([str(b) for b in hqj[2]])
                                            mycursor3 = connection.cursor()
                                            mycursor3.execute("UPDATE calificaciones SET cal_ordinario = %(cal_or3)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as3, "cal_or3":miEntry57.get()})
                                            connection.commit()

                                            id_as4 = "".join([str(b) for b in hqj[3]])
                                            mycursor4 = connection.cursor()
                                            mycursor4.execute("UPDATE calificaciones SET cal_ordinario = %(cal_or4)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as4, "cal_or4":miEntry58.get()})
                                            connection.commit()

                                            id_as5 = "".join([str(b) for b in hqj[4]])
                                            mycursor5 = connection.cursor()
                                            mycursor5.execute("UPDATE calificaciones SET cal_ordinario = %(cal_or5)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as5, "cal_or5":miEntry59.get()})
                                            connection.commit()

                                            id_as6 = "".join([str(b) for b in hqj[5]])
                                            mycursor6 = connection.cursor()
                                            mycursor6.execute("UPDATE calificaciones SET cal_ordinario = %(cal_or6)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as6, "cal_or6":miEntry60.get()})
                                            connection.commit()

                                            id_as7 = "".join([str(b) for b in hqj[6]])
                                            mycursor7 = connection.cursor()
                                            mycursor7.execute("UPDATE calificaciones SET cal_ordinario = %(cal_or7)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as7, "cal_or7":miEntry61.get()})
                                            connection.commit()

                                            id_as8 = "".join([str(b) for b in hqj[7]])
                                            mycursor8 = connection.cursor()
                                            mycursor8.execute("UPDATE calificaciones SET cal_ordinario = %(cal_or8)s WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as8, "cal_or8":miEntry62.get()})
                                            connection.commit()


                                            #Calificaciones finales
                                            mycursor1 = connection.cursor()
                                            ab=int(miEntry19.get())
                                            bc=int(miEntry28.get())
                                            cd=int(miEntry37.get())
                                            de=int(miEntry55.get())
                                            final1 = ((ab + bc + cd + de) / 4)
                                            mycursor1.execute("UPDATE calificaciones SET cal_final = ROUND(%(final1_oficial)s) WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as1, "final1_oficial":final1})
                                            connection.commit()

                                            mycursor2 = connection.cursor()
                                            ac=int(miEntry20.get())
                                            bd=int(miEntry29.get())
                                            ce=int(miEntry38.get())
                                            df=int(miEntry56.get())
                                            final2 = ((ac + bd + ce + df) / 4)
                                            mycursor2.execute("UPDATE calificaciones SET cal_final = ROUND(%(final2_oficial)s) WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as2, "final2_oficial":final2})
                                            connection.commit()

                                            mycursor3 = connection.cursor()
                                            ad=int(miEntry21.get())
                                            be=int(miEntry30.get())
                                            cf=int(miEntry39.get())
                                            dg=int(miEntry57.get())
                                            final3 = ((ad + be + cf + dg) / 4)
                                            mycursor3.execute("UPDATE calificaciones SET cal_final = ROUND(%(final3_oficial)s) WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as3, "final3_oficial":final3})
                                            connection.commit()

                                            mycursor4 = connection.cursor()
                                            ae=int(miEntry22.get())
                                            bf=int(miEntry31.get())
                                            cg=int(miEntry40.get())
                                            dh=int(miEntry58.get())
                                            final4 = ((ae + bf + cg + dh) / 4)
                                            mycursor4.execute("UPDATE calificaciones SET cal_final = ROUND(%(final4_oficial)s) WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as4, "final4_oficial":final4})
                                            connection.commit()

                                            mycursor5 = connection.cursor()
                                            af=int(miEntry23.get())
                                            bg=int(miEntry32.get())
                                            ch=int(miEntry41.get())
                                            di=int(miEntry59.get())
                                            final5 = ((af + bg + ch + di) / 4)
                                            mycursor5.execute("UPDATE calificaciones SET cal_final = ROUND(%(final5_oficial)s) WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as5, "final5_oficial":final5})
                                            connection.commit()

                                            mycursor6 = connection.cursor()
                                            ag=int(miEntry24.get())
                                            bh=int(miEntry33.get())
                                            ci=int(miEntry42.get())
                                            dj=int(miEntry60.get())
                                            final6 = ((ag + bh + ci + dj) / 4)
                                            mycursor6.execute("UPDATE calificaciones SET cal_final = ROUND(%(final6_oficial)s) WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as6, "final6_oficial":final6})
                                            connection.commit()

                                            mycursor7 = connection.cursor()
                                            ah=int(miEntry25.get())
                                            bi=int(miEntry34.get())
                                            cj=int(miEntry43.get())
                                            dk=int(miEntry61.get())
                                            final7 = ((ah + bi + cj + dk) / 4)
                                            mycursor7.execute("UPDATE calificaciones SET cal_final = ROUND(%(final7_oficial)s) WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as7, "final7_oficial":final7})
                                            connection.commit()

                                            #mycursor8 = connection.cursor()
                                            #ai=int(miEntry26.get())
                                            #bj=int(miEntry34.get())
                                            #ck=int(miEntry44.get())
                                            #dl=int(miEntry62.get())
                                            #final8 = ((ai + bj + ck + dl) / 4)
                                            #mycursor8.execute("UPDATE calificaciones SET cal_final = ROUND(%(final8_oficial)s) WHERE FK_id_estudiante = %(id_est)s and FK_id_asignatura = %(id_as)s;", {"id_est":k, "id_as":id_as8, "final8_oficial":final8})
                                            #connection.commit()



                                        #Boton guardar calificaciones insertadas
                                        botonLogin2=Button(miFrame, command=ingreso_calificaciones, text="Guardar",bg="gray75", font=("Arial",15))
                                        botonLogin2.pack()
                                        botonLogin2.place(x=1250, y=120)

                            #Boton aceptar matricula ingresada por el docente
                            BotonMatrícula=Button(miFrame, command=Mostrar_Calif, text="Aceptar",bg="gray75", font=("Arial",10))
                            BotonMatrícula.pack()
                            BotonMatrícula.place(x=670, y=50)


                        miFrame.mainloop()

        else:
            messagebox.showinfo("Advertencia", "Matrícula o contraseña incorrectas")



botonLogin=Button(miFrame, command=abrir_usuario_claves, text="Entrar",bg="gray36", font=("Arial",17), padx=100)
botonLogin.pack()
botonLogin.place(x=170, y=410)


miFrame.mainloop()

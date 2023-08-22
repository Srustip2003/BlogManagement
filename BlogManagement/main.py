elif len(Email)>=12:
            if Email[0].isalpha():
                if ("@" in Email) and (Email.count("@")==1):
                    if (Email[-4]=="."):
                        db=conn.connect(host="localhost",user="root",password="Ashmina27@",database="trail")
                        cursor=db.cursor()
                        cursor.execute("Select * from register where Emailid ='"+Email+"'")
                        row=cursor.fetchone()
                        if row!=None:
                            messagebox.showerror("Error","User already exist, Please Login")
                        else:
                            cursor.execute("INSERT into register(Name,Emailid,Contact,Security_ques,Security_ans,Password) values('"+Namee+"','"+Email+"','"+Contact+"','"+Sques+"',md5('"+Securityans+"'),md5('"+Pass+"'))")
                            db.commit()
                            db.close()
                            messagebox.showinfo("Registration Successfull","Welcome to Pocket Fashion")
                            lp.show()
                            rp.close()
                        
                    else:
                        messagebox.showerror("Error","Enter valid email address with .com")
                else:
                    messagebox.showerror("Error","Enter valid email address with @")
            else:
                messagebox.showerror("Error","First character should be alphabet")
            
        else:
            print("Success")
from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html',boolean = True)  

@auth.route('/logout')
def logout():
    return
    
@auth.route('/sign-up',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        if len(email) < 4:
            flash('Email must be greater than 4 characters',category='error')
        elif  len(first_name) < 3:
            flash('Firstname must be greater than 3 characters',category='error')
        elif  password1 != password2:
            flash('Passwords do not match',category='error')
        elif  len(password1) < 6:
            flash('Passwords must be greater than 6 charachters',category='error')
        else :
            flash('Account created successfully',category='success')
            

    return render_template('sign-up.html')
    


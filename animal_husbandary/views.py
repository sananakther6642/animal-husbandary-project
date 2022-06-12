from random import randint
from io import BytesIO
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import EmailMessage
import hashlib
from django.shortcuts import redirect
import os
from django.shortcuts import HttpResponse
from animal_husbandary.models import customer, food, staflog, animal, vaccine, staff, feedback


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def stafflogin(request):
    return render(request, "stafflogin.html")


def stlog(request):
    emails = request.GET.get('emai')
    pswd = request.GET.get('psw')
    print(emails, pswd)
    d = staflog.objects.filter(email=emails, password=pswd)
    if(d):
        return render(request, 'staffdash.html')
    else:
        messages.warning(request, 'Wrong username or password')
        return render(request, 'stafflogin.html')


def userform(request):
    return render(request, "userform.html")


def ulog(request):
    em = request.GET.get('EmailAddress')
    pasw = request.GET.get('Passwordp')
    pasw = hashlib.md5(pasw.encode('utf-8')).hexdigest()
    print(em, pasw)
    u = customer.objects.filter(email=em, password=pasw)

    if(u):

        response = render(request, 'products.html')
        response.set_cookie('EmailAddress', em)

        return response
    else:
        messages.warning(request, 'Wrong username or password')
        return render(request, 'userform.html')


def regform(request):
    return render(request, "regform.html")


def rform(request):

    nam = request.GET.get('inputname')
    phon = request.GET.get('inputph')
    emai = request.GET.get('inputEmail4')
    passwor = request.GET.get('inputPassword4')
    passwor = hashlib.md5(passwor.encode('utf-8')).hexdigest()
    addres = request.GET.get('inputAddress')
    cit = request.GET.get('inputCity')
    stat = request.GET.get('inputState')
    pincod = request.GET.get('inputZip')
    print(nam, phon, emai, passwor, addres, cit, stat, pincod)

    u = customer(CustomerName=nam, phoneNo=phon, email=emai, password=passwor,
                 Address=addres, city=cit, state=stat, pincode=pincod)
    b = customer.objects.filter(email=emai)
    if(b):
        print("already registered")
        messages.warning(request, 'Email is already registered')
        resa = send_mail(
            "Urgent!!", "User is Already registered Please proceed to login Your Email is \t"+str(u.email), "sananakther11@gmail.com", [emai])
        return render(request, 'userform.html')
    else:

        u.save()

        us = customer.objects.get(email=emai)

        res = send_mail("Registration", "Congratulations!. Your registration is successfull and your customer id " +
                        str(us.customerID) + "" "and email is \t" + str(us.email), "sananakther11@gmail.com", [emai])

        return render(request, 'userform.html')


def deleteuser(request):
    return render(request, "deleteuser.html")


def delr(request):
    emails = request.GET.get('em')
    try:
        c = customer.objects.filter(email=emails)
        print(emails)
        c.delete()
        d = animal.objects.filter(order=emails)
        d.delete()
        print("order deleted")
        print("Record deleted successfully!")

        return redirect(staffdash)
    except:
        return redirect(deleteuser)


def feedbackform(request):
    return render(request, "feedback.html")


def feed(request):
    return render(request, "feed.html")


def fo(request):
    st = food.objects.all()

    istr = '''
    <h2 class="" style="margin-left: 15cm;padding-bottom:0cm; margin-top:-1.7cm; color:#040030"> DATA </h2>
    <table class="table table-striped table-hover table-md" style="height: 50%; border-style:double; border-width:10px; margin-left:3cm; padding-bottom:2cm;">
    <thead class="table ">
    <tr>

    <th style="font-size: 23px; font-weight:bolder; font-family:times roman;margin-left:1cm;color:#731a1a;">FoodID</th>
    <th style="font-size: 25px; font-family:times rpoman;text-align:end;color:#731a1a;padding-left:2cm">QTY(gms)</th>
    <th style="font-size: 25px; font-family:times roman;text-align:end;margin-left:9cm;padding-left:4cm;color:#731a1a;">FOOD ITEM</th>
    <br>
    </tr>
    </td>
    </thead>
    '''

    for bn in st:
        istr += "<tr><td><br>" + str(bn.foodID)+"</td><td>" "</td><td>"+str(bn.quantity) + \
            "</td><td>"+bn.fooditem + "</td><td>"
        # +str(bn.animalID)+"</td><td>"

    return HttpResponse(istr)


def vaccination(request):
    return render(request, "vaccination.html")


def staffinfo(request):
    return render(request, "staffinfo.html")


def staffin(request):
    st = staff.objects.all()
    istr = '''
    <h2 class="" style="margin-left: 17cm;padding-bottom:0cm; margin-top:-1.7cm; color:#040030"> DATA </h2>
    <table class="table table-striped table-hover table-md " style="height: 50%; border-style:double; border-width:10px; margin-left:4cm; padding-bottom:2cm;">
    <thead class="table">
    <tr>

    <th style="font-size: 23px; font-weight:bolder; font-family:times roman;padding-right:1cm;color:#731a1a;">ID</th>
    <th style="font-size: 25px; font-family:times roman; padding-right:1cm;color:#731a1a;margin-left:2cm;">NAME</th>
    <th style="font-size: 25px; font-family:times roman;padding-right:1cm;color:#731a1a;">ADDRESS</th>
    <th style="font-size: 25px; font-family:times roman;padding-right:1cm;color:#731a1a;">PHONE</th>
    <th style="font-size: 25px; font-family:times roman;padding-right:1cm;color:#731a1a;">DESIGNATION</th>
    <th style="font-size: 25px; font-family:times roman;padding-right:-1cm;color:#731a1a;">DATE OF JOIN</th>


    <br>
    </tr>
    </thead>
    '''

    for bn in st:
        istr += "<tr><td><br>" "<br>"+str(bn.staffID)+"</td><td><br>" + \
            bn.staffName+"</td><td><br>"+bn.Address+"</td><td><br>"+str(bn.phone)+"</td><td><br>" + \
            bn.designation + "</td><td><br>"+str(bn.dateofjoin)+"</td><td><br>"

    return HttpResponse(istr)


def vack(request):

    vai = request.GET.get('vaid')
    remak = request.GET.get('rms')
    dat = request.GET.get('da')
    ani = request.GET.get('anid')
    print(vai, remak, dat, ani)
    ua = vaccine(vaccineID=vai, remark=remak,
                 date_of_vaccination=dat, animalID=ani)

    ua.save()

    print("hello")
    a = animal.objects.filter(animalID=ani)
    print(a)
    c = vaccine.objects.filter(vaccineID=vai)
    c.first().vaccinated.add(a.first())

    return render(request, 'staffdash.html')


def staffdash(request):
    return render(request, 'staffdash.html')


def order(request):
    return render(request, 'order.html')


def product(request):
    return render(request, 'products.html')


def search(request):
    return render(request, 'search.html')


def msearch(request):

    animals = request.GET.get('searin')
    anm = animal.objects.filter(typeofanimal=animals)
    istr = '''
    <h2 class="" style="margin-left: 12cm;padding-bottom:1.5cm; color:#040030">Matched Items</h2>
    <table class="table table-striped table-hover table-md" style="width: %; border-style:double; border-width:10px; margin-left:2cm; padding-bottom:2cm;">
    <thead class="table">
    <tr style="font-color:#731a1a;">
    <th class="table"style="font-size: 23px; font-weight:bolder; font-family:times roman;padding-right:20px;color:#731a1a; ">PRODUCTS NAME</th>
    <th style="font-size: 25px; font-family:times roman; padding-right:2cm;color:#731a1a;">PRICE</th>
    <th style="font-size: 25px; font-family:times roman;padding-right:2cm;color:#731a1a;">STATUS</th>
    <th style="font-size: 25px; font-family:times roman;padding-right:2cm;color:#731a1a;">CATEGORY</th>
    <br>
    </tr>
    </thead>
    '''
    for an in anm:
        istr += "<tr><td><br>"+str(an.typeofanimal)+"</td><td><br>" + \
            str(an.price)+"</td><td><br>"+str(an.status) + \
            "</td><td><br>"+an.gender+"</td><td><br>"

    return HttpResponse(istr)


def fd(request):
    inpname = request.GET.get('inpn')
    inpema = request.GET.get('inpem')
    inptets = request.GET.get('inptet')
    inptet21 = request.GET.get('inptet1')

    print(inpname, inpema, inptets, inptet21)
    us = feedback(cname=inpname, email=inpema,
                  suggestion=inptets, improvements=inptet21)

    us.save()
    return render(request, 'home.html')


def coll(request):
    can = animal.objects.all()
    istr = '''
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script>

        function ord(ono)
        {
            $.get("http://127.0.0.1:8000/uorder/",{ono:ono}).done(function(data)
                {
                    $("body").html(data)
                });


        }

    </script>

'''
    cnt = 1
    for ans in can:
        istr += '''

        <div class="grid"  style="padding-top:1cm;padding-right:1cm;"  >

        <div class="card " style="background-color:#d9d9ff;border-style:outset;border-width:5px; border-color:#242482;" >
            <div class="content" style="">
                <h2 id="catt-name">'''+ans.typeofanimal + '''</h2>
                    <img style = "width: 300px; height:230px" src = "http://localhost:8000/static/media/'''+str(cnt)+'''.jpeg" alt = "" >
                    <p class = "pe" > Price: '''+str(ans.price)+''' <span style = "color: rgb(0, 0, 0); font-weight: bold;" > </span> </p>
                             <button type = "button" class = "btn btn-" id = "ordrnow"  onclick = ord('''+str(ans.animalID)+''')  style="font-size:20px;font-weight:bolder; font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif; padding-left:1cm;padding-right:1cm;border-radius:7cm; border-color:#242482;background-color:#050505; color:white;border-style:outset; margin-top:0.2cm; "> Order Now </button>

            </div>
        </div>

        </div>

        '''
        cnt += 1
        if cnt % 10 == 0:
            istr += '''''<div class="grid" ></div>'''''

    return HttpResponse(istr)


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(
        BytesIO(html.encode("iso-8859-1")), result)

    return result.getvalue()


def uorder(request):
    email = request.COOKIES.get('EmailAddress')
    ono = request.GET.get('ono')
    a = animal.objects.filter(animalID=ono)
    print(a)
    c = customer.objects.filter(email=email)
    a.first().order.add(c.first())

    str3 = '''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script&display=swap');

    </style>
    <h1 style="font-size: 2cm;margin-left:3cm; margin-top:2cm; font-family:'Dancing Script', cursive;">THANK YOU  FOR  PLACING  ORDER</h1>
    <div class="container table accordion-header" style="width: 100%;margin-left:-0.2cm; margin-top:1.2cm;padding-bottom:2cm; " id="res">


    <h1 style="font-size: 1.4cm;margin-left:14.5cm; margin-top:2cm; font-family:Roman;">INVOICE</h1>

    <table class="table table-striped table-hover table-md" style="width: 80%; ; border-width:10px; margin-left:6cm; padding-bottom:2cm;">
    <thead class="table">
    <tr>
    <th class="table-info"style="font-size: 25px; font-weight:bolder; font-family:times roman;padding-right:1cm;color:black; ">CUSTOMER DETAILS</th>
    <th class="table-info"style="font-size: 25px; font-family:times roman; padding-right:2cm;color:black;padding-right:1cm;">ORDER ID</th>
    <th class="table-info"style="font-size: 25px; font-family:times roman; padding-right:2cm;color:black;padding-right:1cm;">PRICE</th>
    <th class="table-info"style="font-size: 25px; font-family:times roman; padding-right:2cm;color:black;padding-right:1cm;">Animal Name</th>



    <br>

    </td>
    <br>
    <h2 style="font-size: 0.5cm;margin-left:6cm; text-align:center; font-family:Roman; font-weight:bolder;">COPY OF INVOICE HAS BEEN SENDED TO YOUR EMAIL</h2>
    </thead>


    '''
    for s in c:
        str3 += "</td><td>"+s.email
    for d in a:
        str3 += "</td><td>"+str(d.animalID)+"</td><td>" + \
            str(d.price)+"</td><td>"+str(d.typeofanimal)

    c = customer.objects.get(email=email)
    email = c.email
    a = animal.objects.get(animalID=ono)
    price = float(a.price)
    typeofanimal = a.typeofanimal
    template = 'invoice.html'
    message = "thank you for ordering"
    context = {'ono': ono,  'email': email, 'price': float(
        price), 'typeofanimal': typeofanimal}
    pdf = render_to_pdf(template, context)
    email = EmailMessage("INVOICE", message,
                         "sananakther11@gmail.com", [email])
    email.content_subtype = "pdf"
    email.attach('INVOICE', pdf, 'application/pdf')
    res = email.send()

    return HttpResponse(str3)


def cpass(request):
    return render(request, "cpass.html")


def getotp(request):
    otp = randint(000000, 999999)
    email = request.GET.get('email')
    file_exists = os.path.exists('enm.txt')
    ss = ''
    if file_exists:
        f = open("enm.txt", "r")
        for fh in f:
            s = fh.split(":")
            em = s[0]
            if em == email:
                continue
            s += fh
        f.close()
    f = open("enm.txt", "w")
    ss += email+":"+str(otp)
    f.write(ss)
    f.close()
    send_mail("OTP", "Your OTP is \t" + str(otp),
              "sananakther11@gmail.com", [email])

    return HttpResponse('Mail sent')


def changepass(request):
    email = request.GET.get('email')
    rotp = request.GET.get('rotp')
    npsw = request.GET.get('npsw')
    f = open("enm.txt", "r")
    for fh in f:
        s = fh.split(":")
        em = s[0]
        otp = s[1]
        if em == email and otp == rotp:
            c = customer.objects.get(email=email)
            npsw = hashlib.md5(npsw.encode('utf-8')).hexdigest()
            c.password = npsw
            c.save()

            return HttpResponse("Password changed successfully")

    return HttpResponse("OTP invalid")


def invoice(request):
    return render(request, 'invoice.html')

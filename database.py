import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3360,
    user="root",
    password='',
    database="blood_bank"
)
c = mydb.cursor()

# Terminal
def term_q(abc):
    c.execute(abc)
    data = c.fetchall()
    return data

#Blood

def b_add_data(blood_id, blood_type, d_id, b_no):
    c.execute('INSERT INTO blood(blood_id, blood_type, d_id, b_no) VALUES (%s,%s,%s,%s)', (blood_id, blood_type, d_id, b_no))
    mydb.commit()

def b_view_all_data():
    c.execute('SELECT * FROM blood')
    data = c.fetchall()
    return data

def b_view_only_blood_id():
    c.execute('SELECT blood_id FROM blood')
    data = c.fetchall()
    return data

def b_get_blood(blood_id):
    c.execute('SELECT * FROM blood WHERE blood_id="{}"'.format(blood_id))
    data = c.fetchall()
    return data

def b_edit_blood_data(new_blood_id, new_blood_type, new_d_id, new_b_no, blood_id, blood_type, d_id, b_no):
    c.execute("UPDATE blood SET blood_id=%s, blood_type=%s, d_id=%s, b_no=%s WHERE blood_id=%s and blood_type=%s and d_id=%s and b_no=%s", (new_blood_id, new_blood_type, new_d_id, new_b_no, blood_id, blood_type, d_id, b_no))
    mydb.commit()
    data = c.fetchall()
    return data

def b_delete_data(blood_id):
    c.execute('DELETE FROM blood WHERE blood_id="{}"'.format(blood_id))
    mydb.commit()

#Blood Bank

def bb_add_data(b_no, orders, type, qty, emp_id, hosp_name):
    c.execute('INSERT INTO blood_bank(b_no, orders, type, qty, emp_id, hosp_name) VALUES (%s,%s,%s,%s,%s,%s)',(b_no, orders, type, qty, emp_id, hosp_name))
    mydb.commit()

def bb_view_all_data():
    c.execute('SELECT * FROM blood_bank')
    data = c.fetchall()
    return data

def bb_view_only_blood_id():
    c.execute('SELECT b_no FROM blood_bank')
    data = c.fetchall()
    return data

def bb_get_blood(b_no):
    c.execute('SELECT * FROM blood_bank WHERE b_no="{}"'.format(b_no))
    data = c.fetchall()
    return data

def bb_edit_blood_data(new_b_no, new_orders, new_type, new_qty, new_emp_id, new_hosp_name, b_no, orders, type, qty, emp_id, hosp_name):
    c.execute("UPDATE blood_bank SET b_no=%s, orders=%s, type=%s, qty=%s, emp_id=%s, hosp_name=%s WHERE b_no=%s and orders=%s and type=%s and qty=%s and emp_id=%s and hosp_name=%s", (new_b_no, new_orders, new_type, new_qty, new_emp_id, new_hosp_name, b_no, orders, type, qty, emp_id, hosp_name))
    mydb.commit()
    data = c.fetchall()
    return data

def bb_delete_data(b_no):
    c.execute('DELETE FROM blood_bank WHERE b_no="{}"'.format(b_no))
    mydb.commit()

#Blood Bank Manager

def bbm_add_data(emp_id, name, email_id, phno, b_no):
    c.execute('INSERT INTO blood_bank_manager(emp_id, name, email_id, phno, b_no) VALUES (%s,%s,%s,%s,%s)',(emp_id, name, email_id, phno, b_no))
    mydb.commit()

def bbm_view_all_data():
    c.execute('SELECT * FROM blood_bank_manager')
    data = c.fetchall()
    return data

def bbm_view_only_blood_id():
    c.execute('SELECT emp_id FROM blood_bank_manager')
    data = c.fetchall()
    return data

def bbm_get_blood(emp_id):
    c.execute('SELECT * FROM blood_bank_manager WHERE emp_id="{}"'.format(emp_id))
    data = c.fetchall()
    return data

def bbm_edit_blood_data(new_emp_id, new_name, new_email_id, new_phno, new_b_no, emp_id, name, email_id, phno, b_no):
    c.execute("UPDATE blood_bank_manager SET emp_id=%s, name=%s, email_id=%s, phno=%s, b_no=%s WHERE emp_id=%s and name=%s and email_id=%s and phno=%s and b_no=%s", (new_emp_id, new_name, new_email_id, new_phno, new_b_no, emp_id, name, email_id, phno, b_no))
    mydb.commit()
    data = c.fetchall()
    return data

def bbm_delete_data(emp_id):
    c.execute('DELETE FROM blood_bank_manager WHERE emp_id="{}"'.format(emp_id))
    mydb.commit()

#Blood Stock

def bs_add_data(blood_id, stock_qty, cost):
    c.execute('INSERT INTO blood_stock(blood_id, stock_qty, cost) VALUES (%s,%s,%s)',(blood_id, stock_qty, cost))
    mydb.commit()

def bs_view_all_data():
    c.execute('SELECT * FROM blood_stock')
    data = c.fetchall()
    return data

def bs_view_only_blood_id():
    c.execute('SELECT blood_id FROM blood_stock')
    data = c.fetchall()
    return data

def bs_get_blood(blood_id):
    c.execute('SELECT * FROM blood_stock WHERE blood_id="{}"'.format(blood_id))
    data = c.fetchall()
    return data

def bs_edit_blood_data(new_blood_id, new_stock_qty, new_cost, blood_id, stock_qty, cost):
    c.execute("UPDATE blood_stock SET blood_id=%s, stock_qty=%s, cost=%s WHERE blood_id=%s and stock_qty=%s and cost=%s", (new_blood_id, new_stock_qty, new_cost, blood_id, stock_qty, cost))
    mydb.commit()
    data = c.fetchall()
    return data

def bs_delete_data(blood_id):
    c.execute('DELETE FROM blood_stock WHERE blood_id="{}"'.format(blood_id))
    mydb.commit()

#Donor

def d_add_data(d_id, name, gender, age, address, state, pincode, phno, emp_id):
    c.execute('INSERT INTO donor VALUES (%s,%s,%s,%s)',(d_id, name, gender, age, address, state, pincode, phno, emp_id))
    mydb.commit()

def d_view_all_data():
    c.execute('SELECT * FROM donor')
    data = c.fetchall()
    return data

def d_view_only_blood_id():
    c.execute('SELECT d_id FROM donor')
    data = c.fetchall()
    return data

def d_get_blood(d_id):
    c.execute('SELECT * FROM donor WHERE d_id="{}"'.format(d_id))
    data = c.fetchall()
    return data

def d_edit_blood_data(new_d_id, new_name, new_gender, new_age, new_address, new_state, new_pincode, new_phno, new_emp_id, d_id, name, gender, age, address, state, pincode, phno, emp_id):
    c.execute("UPDATE donor SET d_id=%s, gender=%s, age=%s, address=%s, state=%s, pincode=%s, phno=%s, emp_id=%s WHERE d_id=%s and gender=%s and age=%s and address=%s and state=%s and pincode=%s and phno=%s and emp_id=%s", (new_d_id, new_name, new_gender, new_age, new_address, new_state, new_pincode, new_phno, new_emp_id, d_id, name, gender, age, address, state, pincode, phno, emp_id))
    mydb.commit()
    data = c.fetchall()
    return data

def d_delete_data(d_id):
    c.execute('DELETE FROM donor WHERE d_id="{}"'.format(d_id))
    mydb.commit()

# Hospital

def h_add_data(name, address, phno, b_no, b_no_2):
    c.execute('INSERT INTO hospital VALUES (%s,%s,%s,%s, %s)',(name, address, phno, b_no, b_no_2))
    mydb.commit()

def h_view_all_data():
    c.execute('SELECT * FROM hospital')
    data = c.fetchall()
    return data

def h_view_only_blood_id():
    c.execute('SELECT name FROM hospital')
    data = c.fetchall()
    return data

def h_get_blood(name):
    c.execute('SELECT * FROM hospital WHERE name="{}"'.format(name))
    data = c.fetchall()
    return data

def h_edit_blood_data(new_name, new_address, new_phno, new_b_no, new_b_no_2, name, address, phno, b_no, b_no_2):
    c.execute("UPDATE hospital SET name=%s, address=%s, phno=%s, b_no=%s, b_no_2=%s WHERE name=%s and address=%s and phno=%s and b_no=%s and b_no_2=%s", (new_name, new_address, new_phno, new_b_no, new_b_no_2, name, address, phno, b_no, b_no_2))
    mydb.commit()
    data = c.fetchall()
    return data

def h_delete_data(name):
    c.execute('DELETE FROM hospital WHERE name="{}"'.format(name))
    mydb.commit()

# Receptionist

def r_add_data(emp_id, name, address, phno, b_no):
    c.execute('INSERT INTO receptionist VALUES (%s,%s,%s,%s, %s)',(emp_id, name, address, phno, b_no))
    mydb.commit()

def r_view_all_data():
    c.execute('SELECT * FROM receptionist')
    data = c.fetchall()
    return data

def r_view_only_blood_id():
    c.execute('SELECT emp_id FROM receptionist')
    data = c.fetchall()
    return data

def r_get_blood(emp_id):
    c.execute('SELECT * FROM receptionist WHERE emp_id="{}"'.format(emp_id))
    data = c.fetchall()
    return data

def r_edit_blood_data(new_emp_id, new_name, new_address, new_phno, new_b_no, emp_id, name, address, phno, b_no):
    c.execute("UPDATE receptionist SET emp_id=%s, name=%s, address=%s, phno=%s, b_no=%s WHERE emp_id=%s and name=%s and address=%s and phno=%s and b_no=%s", (new_emp_id, new_name, new_address, new_phno, new_b_no, emp_id, name, address, phno, b_no))
    mydb.commit()
    data = c.fetchall()
    return data

def r_delete_data(emp_id):
    c.execute('DELETE FROM receptionist WHERE emp_id="{}"'.format(emp_id))
    mydb.commit()

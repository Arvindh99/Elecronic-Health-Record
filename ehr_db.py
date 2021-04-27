import sqlite3
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS detailstable(name TEXT,gender TEXT,dob TEXT,contact REAL, blood_group TEXT, pat_his TEXT, doc_name TEXT)')

def add_data(name, gender, dob, contact, blood_group, pat_his, doc_name):
	c.execute('INSERT INTO detailstable(name, gender, dob, contact, blood_group, pat_his, doc_name) VALUES (?,?,?,?,?,?,?)',(name, gender, dob, contact, blood_group, pat_his, doc_name))
	conn.commit()

def view_all_data():
	c.execute('SELECT * FROM detailstable')
	data = c.fetchall()
	return data

def view_all_data_names():
	c.execute('SELECT DISTINCT name FROM detailstable')
	data = c.fetchall()
	return data

def get_name(name):
	c.execute('SELECT * FROM detailstable WHERE name="{}"'.format(name))
	data = c.fetchall()
	return data

def get_contact(contact):
	c.execute('SELECT * FROM detailstable WHERE contact="{}"'.format(contact))
	data = c.fetchall()

def edit_name_data(new_name, new_gender,new_dob, new_contact, new_blood_group, new_pat_his, new_doc_name, name, gender, dob, contact, blood_group, pat_his, doc_name):
	c.execute("UPDATE detailstable SET name =?, gender = ?, dob = ?, contact = ?, blood_group = ?, pat_his = ?, doc_name = ?  WHERE name = ? and gender = ? and dob = ? and contact = ? and blood_group = ? and pat_his = ? and doc_name = ? ",(new_name, new_gender,new_dob, new_contact, new_blood_group, new_pat_his, new_doc_name, name, gender, dob, contact, blood_group, pat_his, doc_name))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(name):
	c.execute('DELETE FROM detailstable WHERE name="{}"'.format(name))
	conn.commit()
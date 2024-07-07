# import module
import smtplib
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



chrome_options = webdriver.EdgeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
print('1')
driver = webdriver.Chrome(options=chrome_options)
#driver = webdriver.Edge(options=chrome_options)


Detect = True 
while(True) : 
    # Create the webdriver object. Here the 
    # chromedriver is present in the driver 
    # folder of the root directory.  
    # get https://www.geeksforgeeks.org/
    driver.get("https://logement.cesal-residentiel.fr/espace-resident/cesal_login.php")
    
    # Maximize the window and let code stall 
    # for 10s to properly maximise the window.
    #driver.maximize_window()
    time.sleep(1)
    
    buttons = driver.find_elements(By.TAG_NAME, "button")
    buttons[1].click()
    time.sleep(1)
    
    buttons = driver.find_elements(By.TAG_NAME, "button")
    email_field = driver.find_element(By.ID, "login-email")
    time.sleep(1)
    email_field.clear()  # Clear the input field (optional)
    email_field.send_keys("elmouslihaymane@gmail.com")  # Fill the email input field
    
    # Find the password input field by its ID
    password_field = driver.find_element(By.ID,"login-password")
    password_field.clear()  # Clear the input field (optional)
    password_field.send_keys("")  # Fill the password input field
    buttons[3].click()
    
    driver.get("https://logement.cesal-residentiel.fr/espace-resident/cesal_mon_logement_reservation.php")
    driver.maximize_window()
    time.sleep(1)
    
    buttons = driver.find_elements(By.TAG_NAME, "button")
    print(buttons)
    date_arrivee_span = driver.find_element(By.ID, "select2-date_arrivee-container")
    date_arrivee_span.click()  # Click on the span to open the dropdown
    
    # Find the desired date option in the dropdown and click on it
    desired_date_option = driver.find_element(By.XPATH,"//ul[@id='select2-date_arrivee-results']/li[last()]")
    desired_date_option.click()
    
    # Find the date sortie input field by its ID
    date_sortie_input = driver.find_element(By.ID,"date_sortie")
    date_sortie_input.clear()  # Clear the input field (optional)
    date_sortie_input.send_keys("30/04/2025")  # Fill the date sortie input field
    
    buttons[4].click()
    time.sleep(1)
    
    
    body = ""
    recipient_email = "salahddin11@gmail.com"
    mail_password = ""
    mail_user = "aymane.el-mouslih@student-cs.fr"
    for k in range(1, 5):
        element_id = f"residence_{k}_logements_disponibles"
        element = driver.find_element(By.ID,element_id)
        text = element.text
        
        if text != "Aucun logement disponible":
            message = f"Yes Dispo Residence {k}!! \n"
            #print(f"Yaay Residence {k} disponible !!")
        else : 
            message = f"No Dispo Residence {k} !!\n"
            #print(f"Nooo Residence {k} indisponible !!")
            
            # Sending email
        subject = "Logement"
        body += message
        print(body)
        
    email_text = f"Subject: {subject}\n\n{body}"
    if "Yes" in body:
        try:
            server = smtplib.SMTP("smtp.office365.com", 587)
            server.ehlo()
            server.starttls()
            server.login(mail_user, mail_password)
            server.sendmail(mail_user, recipient_email, email_text)
            server.close()
            print("Email sent successfully!")
            break
        except Exception as e:
            print("Failed to send email.")
            print(e)
    time.sleep(300)
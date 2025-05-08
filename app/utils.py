import random
import hmac
import hashlib
import time
from django.core.mail import send_mail
from django.conf import settings

def generate_and_send_otp(email):
    try:
        otp_code = ''.join(random.choices('0123456789', k=6))
        expiry_time = int(time.time()) + 300  # OTP valid for 5 minutes
        data = f'{email}{otp_code}{expiry_time}'.encode()
        otp_hash = hmac.new(settings.SECRET_KEY.encode(), data, hashlib.sha256).hexdigest()

        subject = 'Tourism Hike - SignIn OTP Verification'
        message = f'Tourism Hike sign-in OTP code is{otp_code}. It is valid for 5 minutes.'
        from_email = settings.DEFAULT_FROM_EMAIL
        send_mail(subject, message, from_email, [email])

        return otp_hash, expiry_time
    except Exception as e:
        return None, None

def verify_otp(email, otp_code, otp_hash, expiry_time):
    data = f'{email}{otp_code}{expiry_time}'.encode()
    expected_hash = hmac.new(settings.SECRET_KEY.encode(), data, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected_hash, otp_hash) and int(time.time()) < expiry_time

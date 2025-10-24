import re
from typing import Optional


class UserValidation:
    @staticmethod
    def validate_email(email: Optional[str]) -> bool:
        if email is None or email == "":
            return False
        
        email_pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(email_pattern, email):
            return False
        
        if ' ' in email:
            return False
        
        return True

    @staticmethod
    def validate_username(username: Optional[str]) -> bool:
        if username is None or username == "":
            return False
        
        if len(username) < 3 or len(username) > 20:
            return False
        
        username_pattern = r'^[a-zA-Z0-9_]+$'
        
        return bool(re.match(username_pattern, username))

    @staticmethod
    def validate_phone_number(phone: Optional[str]) -> bool:
        if phone is None or phone == "":
            return False
        
        if not phone.isdigit():
            return False
        
        if len(phone) == 11:
            if phone.startswith(('010', '011', '012', '015')):
                return True
        
        if len(phone) == 12:
            if phone.startswith('20') and phone[2:5] in ['10', '11', '12', '15']:
                return True
        
        return False

    @staticmethod
    def validate_national_id(national_id: Optional[str]) -> bool:
        if national_id is None or national_id == "":
            return False
        
        if len(national_id) != 14:
            return False
        
        if not national_id.isdigit():
            return False
        
        century = national_id[0]
        year = national_id[1:3]
        month = national_id[3:5]
        day = national_id[5:7]
        governorate = national_id[7:9]
        
        if century not in ['2', '3']:
            return False
        
        month_int = int(month)
        if month_int < 1 or month_int > 12:
            return False
        
        day_int = int(day)
        if day_int < 1 or day_int > 31:
            return False
        
        governorate_int = int(governorate)
        if governorate_int < 1 or governorate_int > 88:
            return False
        
        return True
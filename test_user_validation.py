import pytest
from user_validation import UserValidation


class TestEmailValidation:
    
    def test_valid_email_format(self):
        email = "user@example.com"
        result = UserValidation.validate_email(email)
        assert result is True
    
    def test_missing_at_symbol(self):
        email = "userexample.com"
        result = UserValidation.validate_email(email)
        assert result is False
    
    def test_missing_domain(self):
        email = "user@"
        result = UserValidation.validate_email(email)
        assert result is False
    
    def test_invalid_tld(self):
        email = "user@mail.c"
        result = UserValidation.validate_email(email)
        assert result is False
    
    def test_email_with_subdomain(self):
        email = "user@mail.company.com"
        result = UserValidation.validate_email(email)
        assert result is True
    
    def test_email_with_special_characters(self):
        email = "mohamed.nabil_21@mail.co"
        result = UserValidation.validate_email(email)
        assert result is True
    
    def test_uppercase_email(self):
        email = "USER@MAIL.COM"
        result = UserValidation.validate_email(email)
        assert result is True
    
    def test_email_with_space(self):
        email = "user name@mail.com"
        result = UserValidation.validate_email(email)
        assert result is False
    
    def test_empty_email(self):
        email = ""
        result = UserValidation.validate_email(email)
        assert result is False
    
    def test_null_input_email(self):
        email = None
        result = UserValidation.validate_email(email)
        assert result is False


class TestUsernameValidation:
    
    def test_valid_username(self):
        username = "ramy_gomaa"
        result = UserValidation.validate_username(username)
        assert result is True
    
    def test_username_too_short(self):
        username = "ab"
        result = UserValidation.validate_username(username)
        assert result is False
    
    def test_username_too_long(self):
        username = "ramygomaaisaverylongusername"
        result = UserValidation.validate_username(username)
        assert result is False
    
    def test_username_with_spaces(self):
        username = "ramy gomaa"
        result = UserValidation.validate_username(username)
        assert result is False
    
    def test_username_with_symbols(self):
        username = "ramy@123"
        result = UserValidation.validate_username(username)
        assert result is False
    
    def test_username_with_digits(self):
        username = "ramy123"
        result = UserValidation.validate_username(username)
        assert result is True
    
    def test_empty_username(self):
        username = ""
        result = UserValidation.validate_username(username)
        assert result is False
    
    def test_null_input_username(self):
        username = None
        result = UserValidation.validate_username(username)
        assert result is False


class TestPhoneNumberValidation:
    
    def test_valid_vodafone_number(self):
        phone = "01012345678"
        result = UserValidation.validate_phone_number(phone)
        assert result is True
    
    def test_valid_orange_number(self):
        phone = "01234567890"
        result = UserValidation.validate_phone_number(phone)
        assert result is True
    
    def test_valid_etisalat_number(self):
        phone = "01198765432"
        result = UserValidation.validate_phone_number(phone)
        assert result is True
    
    def test_valid_we_number(self):
        phone = "01555555555"
        result = UserValidation.validate_phone_number(phone)
        assert result is True
    
    def test_valid_vodafone_with_country_code(self):
        phone = "201012345678"
        result = UserValidation.validate_phone_number(phone)
        assert result is True
    
    def test_valid_orange_with_country_code(self):
        phone = "201234567890"
        result = UserValidation.validate_phone_number(phone)
        assert result is True
    
    def test_invalid_prefix(self):
        phone = "01812345678"
        result = UserValidation.validate_phone_number(phone)
        assert result is False
    
    def test_phone_too_short(self):
        phone = "0101234567"
        result = UserValidation.validate_phone_number(phone)
        assert result is False
    
    def test_phone_too_long(self):
        phone = "010123456789"
        result = UserValidation.validate_phone_number(phone)
        assert result is False
    
    def test_phone_contains_characters(self):
        phone = "01012abc678"
        result = UserValidation.validate_phone_number(phone)
        assert result is False
    
    def test_empty_phone_number(self):
        phone = ""
        result = UserValidation.validate_phone_number(phone)
        assert result is False
    
    def test_null_input_phone(self):
        phone = None
        result = UserValidation.validate_phone_number(phone)
        assert result is False


class TestNationalIdValidation:
    
    def test_valid_national_id(self):
        national_id = "29812251234567"
        result = UserValidation.validate_national_id(national_id)
        assert result is True
    
    def test_national_id_too_short(self):
        national_id = "2981225123456"
        result = UserValidation.validate_national_id(national_id)
        assert result is False
    
    def test_national_id_too_long(self):
        national_id = "298122512345678"
        result = UserValidation.validate_national_id(national_id)
        assert result is False
    
    def test_national_id_contains_letters(self):
        national_id = "2981225AB34567"
        result = UserValidation.validate_national_id(national_id)
        assert result is False
    
    def test_invalid_century_code(self):
        national_id = "19812251234567"
        result = UserValidation.validate_national_id(national_id)
        assert result is False
    
    def test_invalid_month(self):
        national_id = "29813251234567"
        result = UserValidation.validate_national_id(national_id)
        assert result is False
    
    def test_invalid_day(self):
        national_id = "29812323234567"
        result = UserValidation.validate_national_id(national_id)
        assert result is False
    
    def test_invalid_governorate_code(self):
        national_id = "29812380034567"
        result = UserValidation.validate_national_id(national_id)
        assert result is False
    
    def test_empty_national_id(self):
        national_id = ""
        result = UserValidation.validate_national_id(national_id)
        assert result is False
    
    def test_null_input_national_id(self):
        national_id = None
        result = UserValidation.validate_national_id(national_id)
        assert result is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
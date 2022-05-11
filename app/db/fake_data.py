from datetime import datetime
import random
import time
import uuid
import faker.providers
from faker import Faker
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app import crud, schemas

from app.constants.role import Role

from inspect import currentframe, getframeinfo

frameinfo = getframeinfo(currentframe())
cf = currentframe()
filename = getframeinfo(cf).filename
def get_linenumber():
    cf = currentframe()
    return cf.f_back.f_lineno


fakegen = Faker()


def fake_phone_number(fake: Faker) -> str:
    return f"+212 {fake.msisdn()[4:]}"


COUNTRIES_TEMP = [
    {"name": "Afghanistan", "code": "AF"},
    {"name": "land Islands", "code": "AX"},
    {"name": "Albania", "code": "AL"},
    {"name": "Algeria", "code": "DZ"},
]

COUNTRIES = [
    {"name": "Afghanistan", "code": "AF"},
    {"name": "land Islands", "code": "AX"},
    {"name": "Albania", "code": "AL"},
    {"name": "Algeria", "code": "DZ"},
    {"name": "American Samoa", "code": "AS"},
    {"name": "AndorrA", "code": "AD"},
    {"name": "Angola", "code": "AO"},
    {"name": "Anguilla", "code": "AI"},
    {"name": "Antarctica", "code": "AQ"},
    {"name": "Antigua and Barbuda", "code": "AG"},
    {"name": "Argentina", "code": "AR"},
    {"name": "Armenia", "code": "AM"},
    {"name": "Aruba", "code": "AW"},
    {"name": "Australia", "code": "AU"},
    {"name": "Austria", "code": "AT"},
    {"name": "Azerbaijan", "code": "AZ"},
    {"name": "Bahamas", "code": "BS"},
    {"name": "Bahrain", "code": "BH"},
    {"name": "Bangladesh", "code": "BD"},
    {"name": "Barbados", "code": "BB"},
    {"name": "Belarus", "code": "BY"},
    {"name": "Belgium", "code": "BE"},
    {"name": "Belize", "code": "BZ"},
    {"name": "Benin", "code": "BJ"},
    {"name": "Bermuda", "code": "BM"},
    {"name": "Bhutan", "code": "BT"},
    {"name": "Bolivia", "code": "BO"},
    {"name": "Bosnia and Herzegovina", "code": "BA"},
    {"name": "Botswana", "code": "BW"},
    {"name": "Bouvet Island", "code": "BV"},
    {"name": "Brazil", "code": "BR"},
    {"name": "British Indian Ocean Territory", "code": "IO"},
    {"name": "Brunei Darussalam", "code": "BN"},
    {"name": "Bulgaria", "code": "BG"},
    {"name": "Burkina Faso", "code": "BF"},
    {"name": "Burundi", "code": "BI"},
    {"name": "Cambodia", "code": "KH"},
    {"name": "Cameroon", "code": "CM"},
    {"name": "Canada", "code": "CA"},
    {"name": "Cape Verde", "code": "CV"},
    {"name": "Cayman Islands", "code": "KY"},
    {"name": "Central African Republic", "code": "CF"},
    {"name": "Chad", "code": "TD"},
    {"name": "Chile", "code": "CL"},
    {"name": "China", "code": "CN"},
    {"name": "Christmas Island", "code": "CX"},
    {"name": "Cocos (Keeling) Islands", "code": "CC"},
    {"name": "Colombia", "code": "CO"},
    {"name": "Comoros", "code": "KM"},
    {"name": "Congo", "code": "CG"},
    {"name": "Congo, The Democratic Republic of the", "code": "CD"},
    {"name": "Cook Islands", "code": "CK"},
    {"name": "Costa Rica", "code": "CR"},
    {"name": "Cote D'Ivoire", "code": "CI"},
    {"name": "Croatia", "code": "HR"},
    {"name": "Cuba", "code": "CU"},
    {"name": "Cyprus", "code": "CY"},
    {"name": "Czech Republic", "code": "CZ"},
    {"name": "Denmark", "code": "DK"},
    {"name": "Djibouti", "code": "DJ"},
    {"name": "Dominica", "code": "DM"},
    {"name": "Dominican Republic", "code": "DO"},
    {"name": "Ecuador", "code": "EC"},
    {"name": "Egypt", "code": "EG"},
    {"name": "El Salvador", "code": "SV"},
    {"name": "Equatorial Guinea", "code": "GQ"},
    {"name": "Eritrea", "code": "ER"},
    {"name": "Estonia", "code": "EE"},
    {"name": "Ethiopia", "code": "ET"},
    {"name": "Falkland Islands (Malvinas)", "code": "FK"},
    {"name": "Faroe Islands", "code": "FO"},
    {"name": "Fiji", "code": "FJ"},
    {"name": "Finland", "code": "FI"},
    {"name": "France", "code": "FR"},
    {"name": "French Guiana", "code": "GF"},
    {"name": "French Polynesia", "code": "PF"},
    {"name": "French Southern Territories", "code": "TF"},
    {"name": "Gabon", "code": "GA"},
    {"name": "Gambia", "code": "GM"},
    {"name": "Georgia", "code": "GE"},
    {"name": "Germany", "code": "DE"},
    {"name": "Ghana", "code": "GH"},
    {"name": "Gibraltar", "code": "GI"},
    {"name": "Greece", "code": "GR"},
    {"name": "Greenland", "code": "GL"},
    {"name": "Grenada", "code": "GD"},
    {"name": "Guadeloupe", "code": "GP"},
    {"name": "Guam", "code": "GU"},
    {"name": "Guatemala", "code": "GT"},
    {"name": "Guernsey", "code": "GG"},
    {"name": "Guinea", "code": "GN"},
    {"name": "Guinea-Bissau", "code": "GW"},
    {"name": "Guyana", "code": "GY"},
    {"name": "Haiti", "code": "HT"},
    {"name": "Heard Island and Mcdonald Islands", "code": "HM"},
    {"name": "Holy See (Vatican City State)", "code": "VA"},
    {"name": "Honduras", "code": "HN"},
    {"name": "Hong Kong", "code": "HK"},
    {"name": "Hungary", "code": "HU"},
    {"name": "Iceland", "code": "IS"},
    {"name": "India", "code": "IN"},
    {"name": "Indonesia", "code": "ID"},
    {"name": "Iran, Islamic Republic Of", "code": "IR"},
    {"name": "Iraq", "code": "IQ"},
    {"name": "Ireland", "code": "IE"},
    {"name": "Isle of Man", "code": "IM"},
    {"name": "Israel", "code": "IL"},
    {"name": "Italy", "code": "IT"},
    {"name": "Jamaica", "code": "JM"},
    {"name": "Japan", "code": "JP"},
    {"name": "Jersey", "code": "JE"},
    {"name": "Jordan", "code": "JO"},
    {"name": "Kazakhstan", "code": "KZ"},
    {"name": "Kenya", "code": "KE"},
    {"name": "Kiribati", "code": "KI"},
    {"name": "Korea, Democratic People'S Republic of", "code": "KP"},
    {"name": "Korea, Republic of", "code": "KR"},
    {"name": "Kuwait", "code": "KW"},
    {"name": "Kyrgyzstan", "code": "KG"},
    {"name": "Lao People'S Democratic Republic", "code": "LA"},
    {"name": "Latvia", "code": "LV"},
    {"name": "Lebanon", "code": "LB"},
    {"name": "Lesotho", "code": "LS"},
    {"name": "Liberia", "code": "LR"},
    {"name": "Libyan Arab Jamahiriya", "code": "LY"},
    {"name": "Liechtenstein", "code": "LI"},
    {"name": "Lithuania", "code": "LT"},
    {"name": "Luxembourg", "code": "LU"},
    {"name": "Macao", "code": "MO"},
    {
        "name": "Macedonia, The Former Yugoslav Republic of",
        "code": "MK",
    },
    {"name": "Madagascar", "code": "MG"},
    {"name": "Malawi", "code": "MW"},
    {"name": "Malaysia", "code": "MY"},
    {"name": "Maldives", "code": "MV"},
    {"name": "Mali", "code": "ML"},
    {"name": "Malta", "code": "MT"},
    {"name": "Marshall Islands", "code": "MH"},
    {"name": "Martinique", "code": "MQ"},
    {"name": "Mauritania", "code": "MR"},
    {"name": "Mauritius", "code": "MU"},
    {"name": "Mayotte", "code": "YT"},
    {"name": "Mexico", "code": "MX"},
    {"name": "Micronesia, Federated States of", "code": "FM"},
    {"name": "Moldova, Republic of", "code": "MD"},
    {"name": "Monaco", "code": "MC"},
    {"name": "Mongolia", "code": "MN"},
    {"name": "Montenegro", "code": "ME"},
    {"name": "Montserrat", "code": "MS"},
    {"name": "Morocco", "code": "MA"},
    {"name": "Mozambique", "code": "MZ"},
    {"name": "Myanmar", "code": "MM"},
    {"name": "Namibia", "code": "NA"},
    {"name": "Nauru", "code": "NR"},
    {"name": "Nepal", "code": "NP"},
    {"name": "Netherlands", "code": "NL"},
    {"name": "Netherlands Antilles", "code": "AN"},
    {"name": "New Caledonia", "code": "NC"},
    {"name": "New Zealand", "code": "NZ"},
    {"name": "Nicaragua", "code": "NI"},
    {"name": "Niger", "code": "NE"},
    {"name": "Nigeria", "code": "NG"},
    {"name": "Niue", "code": "NU"},
    {"name": "Norfolk Island", "code": "NF"},
    {"name": "Northern Mariana Islands", "code": "MP"},
    {"name": "Norway", "code": "NO"},
    {"name": "Oman", "code": "OM"},
    {"name": "Pakistan", "code": "PK"},
    {"name": "Palau", "code": "PW"},
    {"name": "Palestinian Territory, Occupied", "code": "PS"},
    {"name": "Panama", "code": "PA"},
    {"name": "Papua New Guinea", "code": "PG"},
    {"name": "Paraguay", "code": "PY"},
    {"name": "Peru", "code": "PE"},
    {"name": "Philippines", "code": "PH"},
    {"name": "Pitcairn", "code": "PN"},
    {"name": "Poland", "code": "PL"},
    {"name": "Portugal", "code": "PT"},
    {"name": "Puerto Rico", "code": "PR"},
    {"name": "Qatar", "code": "QA"},
    {"name": "Reunion", "code": "RE"},
    {"name": "Romania", "code": "RO"},
    {"name": "Russian Federation", "code": "RU"},
    {"name": "RWANDA", "code": "RW"},
    {"name": "Saint Helena", "code": "SH"},
    {"name": "Saint Kitts and Nevis", "code": "KN"},
    {"name": "Saint Lucia", "code": "LC"},
    {"name": "Saint Pierre and Miquelon", "code": "PM"},
    {"name": "Saint Vincent and the Grenadines", "code": "VC"},
    {"name": "Samoa", "code": "WS"},
    {"name": "San Marino", "code": "SM"},
    {"name": "Sao Tome and Principe", "code": "ST"},
    {"name": "Saudi Arabia", "code": "SA"},
    {"name": "Senegal", "code": "SN"},
    {"name": "Serbia", "code": "RS"},
    {"name": "Seychelles", "code": "SC"},
    {"name": "Sierra Leone", "code": "SL"},
    {"name": "Singapore", "code": "SG"},
    {"name": "Slovakia", "code": "SK"},
    {"name": "Slovenia", "code": "SI"},
    {"name": "Solomon Islands", "code": "SB"},
    {"name": "Somalia", "code": "SO"},
    {"name": "South Africa", "code": "ZA"},
    {
        "name": "South Georgia and the South Sandwich Islands",
        "code": "GS",
    },
    {"name": "Spain", "code": "ES"},
    {"name": "Sri Lanka", "code": "LK"},
    {"name": "Sudan", "code": "SD"},
    {"name": "Suriname", "code": "SR"},
    {"name": "Svalbard and Jan Mayen", "code": "SJ"},
    {"name": "Swaziland", "code": "SZ"},
    {"name": "Sweden", "code": "SE"},
    {"name": "Switzerland", "code": "CH"},
    {"name": "Syrian Arab Republic", "code": "SY"},
    {"name": "Taiwan, Province of China", "code": "TW"},
    {"name": "Tajikistan", "code": "TJ"},
    {"name": "Tanzania, United Republic of", "code": "TZ"},
    {"name": "Thailand", "code": "TH"},
    {"name": "Timor-Leste", "code": "TL"},
    {"name": "Togo", "code": "TG"},
    {"name": "Tokelau", "code": "TK"},
    {"name": "Tonga", "code": "TO"},
    {"name": "Trinidad and Tobago", "code": "TT"},
    {"name": "Tunisia", "code": "TN"},
    {"name": "Turkey", "code": "TR"},
    {"name": "Turkmenistan", "code": "TM"},
    {"name": "Turks and Caicos Islands", "code": "TC"},
    {"name": "Tuvalu", "code": "TV"},
    {"name": "Uganda", "code": "UG"},
    {"name": "Ukraine", "code": "UA"},
    {"name": "United Arab Emirates", "code": "AE"},
    {"name": "United Kingdom", "code": "GB"},
    {"name": "United States", "code": "US"},
    {"name": "United States Minor Outlying Islands", "code": "UM"},
    {"name": "Uruguay", "code": "UY"},
    {"name": "Uzbekistan", "code": "UZ"},
    {"name": "Vanuatu", "code": "VU"},
    {"name": "Venezuela", "code": "VE"},
    {"name": "Viet Nam", "code": "VN"},
    {"name": "Virgin Islands, British", "code": "VG"},
    {"name": "Virgin Islands, U.S.", "code": "VI"},
    {"name": "Wallis and Futuna", "code": "WF"},
    {"name": "Western Sahara", "code": "EH"},
    {"name": "Yemen", "code": "YE"},
    {"name": "Zambia", "code": "ZM"},
    {"name": "Zimbabwe", "code": "ZW"},
]

x_FORM_ELEMENT_TYPES_x = {
    "button": "button",
    "checkbox": "checkbox",
    "date": "date",
    "email": "email",
    "select": "select",
    "radio": "radio",
    "tel": "tel",
    "text": "text",
    "text_area": "text_area",
    "url": "url",
}


FORM_ELEMENT_TYPES = [
    {"type": "input"},
    {"type": "radiobutton"},
    {"type": "checkbox"},
    {"type": "select"},
    {"type": "date"},
]

FORM_ELEMENT_INPUT_TYPES = [
    {"input_type": "text"},
    {"input_type": "email"},
    {"input_type": "password"},
]

VALIDATORS = [
    {"name": "required"},
    {"name": "pattern"},
]

ESSENTIAL_FORM_ELEMENTS = [
    {
        "type": "input",
        "label": "Text",
        "inputType": "text",
        "name": "text",
        "value": "text",
        "description": "Single line of text",
        "validations": [
            {
                "validator": {"name": "required"},
                "message": "Text Required",
            },
        ],
    },
    {
        "type": "input",
        "label": "Email Address",
        "inputType": "email",
        "name": "email",
        "value": "",
        "description": "Email validation input",
        "validations": [
            {
                "validator": {"name": "required"},
                "message": "Email Required",
            },
            {
                "validator": {"name": "pattern"},
                "pattern": "^[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,4}$",
                "message": "Invalid email",
            },
        ],
    },
    {
        "type": "input",
        "label": "Password",
        "inputType": "password",
        "name": "password",
        "value": "",
        "description": "Masked characters input",
        "validations": [
            {
                "validator": {"name": "required"},
                "message": "Password Required",
            },
        ],
    },
    {
        "type": "radiobutton",
        "label": "Single Selection",
        "name": "single_selection",
        "options": [
            {
                "value": "male",
            },
            {
                "value": "female",
            },
        ],
        "value": "",
        "description": "Select only one item with a radio button",
        "validations": [],
    },
    {
        "type": "checkbox",
        "label": "Multiple Selection",
        "name": "multiple_selection",
        "value": [],
        "options": [],
        "description": "Select one or many options using a checkbox",
        "validations": [],
    },
    {
        "type": "select",
        "label": "Select from List",
        "name": "select_from_list",
        "value": "",
        "options": [],
        "description": "Select option from list",
        "validations": [],
    },
    {
        "type": "date",
        "label": "Date",
        "name": "date",
        "value": "",
        "description": "Select a date from a datepicker",
        "validations": [
            {
                "validator": {"name": "required"},
                "message": "Date is Required",
            },
        ],
    },
]

FORM_ELEMENT_NAMES = [
    {"name": "Full name", "type": "text"},
    {"name": "First name", "type": "text"},
    {"name": "Last name", "type": "text"},
    {"name": "Middle name", "type": "text"},
    {"name": "Gender", "type": "radio"},
    {"name": "Phone", "type": "tel"},
    {"name": "Date of birth", "type": "date"},
    {"name": "Email", "type": "email"},
    {"name": "Address", "type": "text"},
    {"name": "Country", "type": "select"},
    {"name": "Zip code", "type": "text"},
]

GENDERS = ["male", "female"]


class Provider(faker.providers.BaseProvider):
    def form_element_name(self):
        return self.random_element(FORM_ELEMENT_NAMES)


fakegen.add_provider(Provider)


def is_pattern(validation):
    return (
        validation["pattern"]
        if (
            ("validator" in validation)
            and (validation["validator"]["name"] == "pattern")
        )
        else None
    )


def fake_data(db: Session) -> None:
    start_time = time.time()
    # Create user for each role except super admin
    members = [
        attr
        for attr in dir(Role)
        if not callable(getattr(Role, attr))
        and not attr.startswith("__")
    ]
    for role_name in members:
        if role_name != Role.SUPER_ADMIN["name"]:
            # Create user
            name = fakegen.name()
            word = fakegen.word()
            first_name = name.split(" ")[0]
            last_name = " ".join(name.split(" ")[-1:])
            domain = "gmail"
            username = first_name[
                0
            ].lower() + last_name.lower().replace(" ", "")
            email = word + "@" + domain + ".com"
            phone_number = fake_phone_number(fakegen)
            password = "1234"
            user_in = schemas.UserCreate(
                email=email,
                password=password,
                full_name=first_name + " " + last_name,
                phone_number=phone_number,
            )
            user = crud.user.create(db, obj_in=user_in)
            # Assign super_admin role to user
            user_role = crud.user_role.get_by_user_id(
                db, user_id=user.id
            )
            if not user_role:
                role = crud.role.get_by_name(
                    db, name=getattr(Role, role_name)["name"]
                )
                user_role_in = schemas.UserRoleCreate(
                    user_id=user.id, role_id=role.id
                )
                crud.user_role.create(db, obj_in=user_role_in)

    # Create Clients
    clients_in = list()
    for _ in range(20):
        name = fakegen.name()
        word = fakegen.word()
        first_name = name.split(" ")[0]
        last_name = " ".join(name.split(" ")[-1:])
        domain = "gmail"
        username = first_name[0].lower() + last_name.lower().replace(
            " ", ""
        )
        number = random.randint(1111,9999)
        email = word + str(number) + "@" + domain + ".com"
        phone_number = fake_phone_number(fakegen)
        client = crud.client.get_by_email(db, email=email)
        if not client:
            client_in = schemas.ClientCreate(
                # name=settings.FIRST_SUPER_ADMIN_CLIENT_NAME,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                user_id="1",
            )
            clients_in.append(client_in)
            # crud.client.create(db, obj_in=client_in)
    crud.client.bulk_create(db, objs_in=clients_in)
            
    # crud.validator.coco(db)
    # Create licenses
    licenses_in = list()
    for _ in range(40):
        license_in = schemas.LicenseCreate(
            key=uuid.uuid4().hex,
            description=fakegen.sentence(),
            type=random.choice(["SIMPLE", "CUSTOM"]),
            # expiry=datetime.strptime('1990-09-06', '%Y-%m-%d')
            # expiry=datetime.strptime("12/11/2018 09:15:32", "%d/%m/%Y %H:%M:%S")
            status=random.choice([True, False]),
            expiry=datetime.strptime(
                fakegen.date_time_between(
                    start_date="+1y", end_date="+6y"
                ).strftime("%d-%m-%Y %H:%M:%S"),
                "%d-%m-%Y %H:%M:%S",
            ),
            # expiry=datetime.date("2000-10-14"),
            # expiry=datetime.utcnow,
            # expiry=datetime(2012, 3, 3, 10, 10, 10),
            product_id=random.randint(1, 10),
            client_id=random.randint(1, 20),
            # expiry=fakegen.date_time().strftime("%d-%m-%Y %H:%M:%S")
            # expiry='test'
        )
        licenses_in.append(license_in)
        # print("datetime.strptime('1990-09-06', '%Y-%m-%d')");
        # print(datetime.strptime('1990-09-06', '%Y-%m-%d'))
        # crud.license.create(db, obj_in=license_in)
    crud.license.bulk_create(db, objs_in=licenses_in)
    
    # Create products
    products_in = list()
    for _ in range(10):
        product_in = schemas.ProductCreate(
            name=fakegen.company(),
            description=fakegen.sentence(),
            form_id=2
        )
        products_in.append(product_in)
        # crud.product.create(db, obj_in=product_in)
    crud.product.bulk_create(db, objs_in=products_in)
    # Assign license to plan
    # user_roles_in = list()
    # for _ in range(10):
    #     i = _ + 1
    #     user_role_in = schemas.PlanCreate(
    #         license_id=str(i), product_id=str(i)
    #     )
    #     user_roles_in.append(user_role_in)
    #     # crud.plan.create(db, obj_in=user_role_in)
    # crud.plan.bulk_create(db, objs_in=user_roles_in)
    
    # Create simple licenses & custom licenses
    all_license = crud.license.get_multi(db)
    # simple_licenses_in = list()
    custom_licenses_in = list()
    for field in all_license:
        # if field.type == "SIMPLE":
        #     simple_license_in = schemas.SimpleLicenseCreate(
        #         device_name=fakegen.first_name() + "-PC",
        #         license_id=field.id,
        #     )
        #     simple_licenses_in.append(simple_license_in)
            # crud.simple_license.create(db, obj_in=simple_license_in)
        if field.type == "CUSTOM":
            custom_license_in = schemas.CustomLicenseCreate(
                license_id=field.id
            )
            custom_licenses_in.append(custom_license_in)
            # crud.custom_license.create(db, obj_in=custom_license_in)
    # crud.simple_license.bulk_create(db, objs_in=simple_licenses_in)
    crud.custom_license.bulk_create(db, objs_in=custom_licenses_in)
    
    # Create forms
    # for _ in range(10):
    # form_in = schemas.FormCreate(name=fakegen.word())
    # form_in = schemas.FormCreate(name="essential fields")
    # create essential fields form
    form_in = schemas.FormCreate()
    crud.form.create(db, obj_in=form_in)
    # Create form element types
    form_element_types_in = list()
    for form_element_type_item in FORM_ELEMENT_TYPES:
        form_element_type_in = schemas.FormElementTypeCreate(
            name=form_element_type_item["type"],
        )
        form_element_types_in.append(form_element_type_in)
        # crud.form_element_type.create(
        #     db, obj_in=form_element_type_in
        # )
    crud.form_element_type.bulk_create(
        db, objs_in=form_element_types_in
    )
    # Create form element input types
    # form_element_type_model = crud.form_element_type.get_by_name(
    #     db, name="input"
    # )
    # for form_element_input_type in FORM_ELEMENT_INPUT_TYPES:
    #     form_element_input_type_in = (
    #         schemas.FormElementInputTypeCreate(
    #             input_type=form_element_input_type["input_type"],
    #             form_element_type_id=form_element_type_model.id,
    #         )
    #     )
    #     crud.form_element_input_type.create(
    #         db, obj_in=form_element_input_type_in
    #     )
    # Create validators
    validators_in = list()
    for validator in VALIDATORS:
        validator_in = schemas.ValidatorCreate(
            name=validator["name"],
        )
        validators_in.append(validator_in)
        # crud.validator.create(db, obj_in=validator_in)
    crud.validator.bulk_create(db, objs_in=validators_in)
    
    # Create validations
    for essential_form_element in ESSENTIAL_FORM_ELEMENTS:
        #     # Create form element input types
        #     form_element_input_type
        #     if essential_form_element.inputType:
        #         form_element_input_type_in = (
        #             schemas.FormElementInputTypeCreate(
        #                 name=essential_form_element.inputType,
        #                 description=essential_form_element.description,
        #             )
        #         )
        #         form_element_input_type = (
        #             crud.form_element_input_type.create(
        #                 db, obj_in=form_element_input_type_in
        #             )
        #         )
        #     # Create form element types
        #     if form_element_input_type:
        #         form_element_type_in = schemas.FormElementTypeCreate(
        #             type=essential_form_element.type,
        #             name=essential_form_element.name,
        #             form_element_input_type_id=form_element_input_type.id,
        #         )
        #         form_element_type = crud.form_element_type.create(
        #             db, obj_in=form_element_type_in
        #         )
        #     else:
        #         form_element_type_in = schemas.FormElementTypeCreate(
        #             type=essential_form_element.type,
        #             name=essential_form_element.name,
        #         )
        #         form_element_type = crud.form_element_type.create(
        #             db, obj_in=form_element_type_in
        #         )
        # Create form element templates
        form_element_type = crud.form_element_type.get_by_name(
            db, name=essential_form_element["type"]
        )
        form_element_template_in = schemas.FormElementTemplateCreate(
            name=essential_form_element["name"],
            description=essential_form_element["description"],
            form_element_type_id=form_element_type.id,
        )
        form_element_template = crud.form_element_template.create(
            db, obj_in=form_element_template_in
        )
        # Create form element fields
        form_element_field_in = schemas.FormElementFieldCreate(
            name=essential_form_element["label"],
            form_element_template_id=form_element_template.id,
            form_id=1,
        )
        crud.form_element_field.create(
            db, obj_in=form_element_field_in
        )
        # Create Validations for the form element
        for validation in essential_form_element["validations"]:
            if len(validation) > 0:
                validator = crud.validator.get_by_name(
                    db, name=validation["validator"]["name"]
                )
                validation_in = schemas.ValidationCreate(
                    message=validation["message"],
                    validator_id=validator.id,
                    form_element_template_id=form_element_template.id,
                    # pattern=validation["pattern"],
                    pattern=is_pattern(validation),
                )
                crud.validation.create(db, obj_in=validation_in)
        # Create form element option for the form element template
        # if "options" in essential_form_element:
        #     for form_element_option in essential_form_element[
        #         "options"
        #     ]:
        #         if len(form_element_option) > 0:
        #             form_element_option_in = schemas.FormElementOptionCreate(
        #                 value=form_element_option["value"],
        #                 form_element_template_id=form_element_template.id,
        #             )
        #             crud.form_element_option.create(
        #                 db, obj_in=form_element_option_in
        #             )

    # # Create form element types
    # for name in FORM_ELEMENT_TYPES:
    #     form_element_type_in = schemas.FormElementTypeCreate(
    #         name=name
    #     )
    #     crud.form_element_type.create(
    #         db, obj_in=form_element_type_in
    #     )
    # # Create form elements with type
    # for field in FORM_ELEMENT_NAMES:
    #     form_element_type = crud.form_element_type.get_by_name(
    #         db, name=field["type"]
    #     )
    #     form_element_in = schemas.FormElementCreate(
    #         name=field["name"],
    #         form_element_type_id=form_element_type.id,
    #     )
    #     crud.form_element_template.create(db, obj_in=form_element_in)

    # Create form element options
    # Single Selection
    # OPTIONS = [
    #     {
    #         "name": "male",
    #     },
    #     {
    #         "name": "female",
    #     },
    # ]
    # form_element_field = crud.form_element_field.get_by_name(
    #     db, name="Single Selection"
    # )

    # # start_time = time.time()
    # form_element_options_in = list()
    # for field in OPTIONS:
    #     form_element_option_in = (
    #         schemas.FormElementOptionCreate(
    #             name=field["name"],
    #             form_element_field_id=form_element_field.id,
    #         )
    #     )

    #     form_element_options_in.append(
    #         form_element_option_in
    #     )
    #     # crud.form_element_option.create(
    #     #     db, obj_in=form_element_option_in
    #     # )
    # crud.form_element_option.bulk_create(
    #     db, objs_in=form_element_options_in
    # )
    
    # Multiple Selection
    # form_element_field = crud.form_element_field.get_by_name(
    #     db, name="Multiple Selection"
    # )

    # form_element_options_in = list()
    # for field in COUNTRIES:
    #     form_element_option_in = (
    #         schemas.FormElementOptionCreate(
    #             name=field["name"],
    #             form_element_field_id=form_element_field.id,
    #         )
    #     )

    #     form_element_options_in.append(
    #         form_element_option_in
    #     )
    #     # crud.form_element_option.create(
    #     #     db, obj_in=form_element_option_in
    #     # )
    # crud.form_element_option.bulk_create(
    #     db, objs_in=form_element_options_in
    # )
    print("the next line from:   ", filename, get_linenumber()+1)
    print("--- populate db in %s seconds ---" % (time.time() - start_time))

    # form_element_template = crud.form_element_template.get_by_name(db, name="Gender")
    # for field in GENDERS:
    #     form_element_option_in = (
    #         schemas.FormElementOptionCreate(
    #             value=field, form_element_template_id=form_element_template.id
    #         )
    #     )
    #     crud.form_element_option.create(
    #         db, obj_in=form_element_option_in
    #     )

    # Create selected value
    # FAKE_FORM_ELEMENT = [
    #     {"name": "Full name", "value": "john doe"},
    #     {"name": "Gender", "value": "male"},
    #     {"name": "Country", "value": "morocco"},
    # ]
    # for field in FAKE_FORM_ELEMENT:
    #     form_element_template = crud.form_element_template.get_by_name(
    #         db, name=field["name"]
    #     )
    #     # Assign a form to form element
    #     form_element_field_in = schemas.FormElementFieldCreate(
    #         form_element_template_id=form_element_template.id,
    #         form_id=1,
    #     )
    #     crud.form_element_field.create(
    #         db, obj_in=form_element_field_in
    #     )

    #     # Assign a form to a custom license
    #     custom_license_in = schemas.CustomLicenseCreate(
    #         license_id=3, form_id=1
    #     )
    #     custom_license = crud.custom_license.get(db, obj_id=3)
    #     crud.custom_license.update(
    #         db, db_obj=custom_license, obj_in=custom_license_in
    #     )

    #     form_element_type = crud.form_element_type.get(
    #         db, obj_id=form_element_template.form_element_type_id
    #     )
    #     if form_element_type.name in ["radio", "checkbox", "select"]:
    #         selected_value_in = schemas.SelectedValueCreate(
    #             value=None,
    #             form_element_template_id=form_element_template.id,
    #             client_id="1",
    #         )
    #         selected_value = crud.selected_value.create(
    #             db, obj_in=selected_value_in
    #         )
    #         # Assign selected value to form element option
    #         form_element_option = crud.form_element_option.get_by_name_and_form_element_id(
    #             db,
    #             form_element_template_id=form_element_template.id,
    #             value=field["value"],
    #         )
    #         selected_list_value_in = schemas.SelectedListValueCreate(
    #             selected_value_id=selected_value.id,
    #             form_element_option_id=form_element_option.id,
    #         )
    #         crud.selected_list_value.create(
    #             db, obj_in=selected_list_value_in
    #         )
    #     else:
    #         selected_value_in = schemas.SelectedValueCreate(
    #             value=field["value"],
    #             form_element_template_id=form_element_template.id,
    #             client_id="1",
    #         )
    #         selected_value = crud.selected_value.create(
    #             db, obj_in=selected_value_in
    #         )
    
    # # Create selected value
    # FAKE_FORM_ELEMENT = [
    #     {"name": "Full name", "value": "john doe"},
    #     {"name": "Gender", "value": "male"},
    #     {"name": "Country", "value": "morocco"},
    # ]
    # for field in FAKE_FORM_ELEMENT:
    #     form_element_template = crud.form_element_template.get_by_name(
    #         db, name=field["name"]
    #     )
    #     # Assign a form to form element
    #     form_element_field_in = schemas.FormElementFieldCreate(
    #         form_element_template_id=form_element_template.id,
    #         form_id=1,
    #     )
    #     crud.form_element_field.create(
    #         db, obj_in=form_element_field_in
    #     )

    #     # Assign a form to a custom license
    #     custom_license_in = schemas.CustomLicenseCreate(
    #         license_id=3, form_id=1
    #     )
    #     custom_license = crud.custom_license.get(db, obj_id=3)
    #     crud.custom_license.update(
    #         db, db_obj=custom_license, obj_in=custom_license_in
    #     )

    #     form_element_type = crud.form_element_type.get(
    #         db, obj_id=form_element_template.form_element_type_id
    #     )
    #     if form_element_type.name in ["radio", "checkbox", "select"]:
    #         selected_value_in = schemas.SelectedValueCreate(
    #             value=None,
    #             form_element_template_id=form_element_template.id,
    #             client_id="1",
    #         )
    #         selected_value = crud.selected_value.create(
    #             db, obj_in=selected_value_in
    #         )
    #         # Assign selected value to form element option
    #         form_element_option = crud.form_element_option.get_by_name_and_form_element_id(
    #             db,
    #             form_element_template_id=form_element_template.id,
    #             value=field["value"],
    #         )
    #         selected_list_value_in = schemas.SelectedListValueCreate(
    #             selected_value_id=selected_value.id,
    #             form_element_option_id=form_element_option.id,
    #         )
    #         crud.selected_list_value.create(
    #             db, obj_in=selected_list_value_in
    #         )
    #     else:
    #         selected_value_in = schemas.SelectedValueCreate(
    #             value=field["value"],
    #             form_element_template_id=form_element_template.id,
    #             client_id="1",
    #         )
    #         selected_value = crud.selected_value.create(
    #             db, obj_in=selected_value_in
    #         )

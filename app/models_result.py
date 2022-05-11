collected_data = {
    "form_id": "2",
    "name": "Test",
    "client_id": "11",
    "form_element_templates": [
        {"name": "Full name", "value": "john doe"},
        {"name": "Gender", "value": "male"},
        {"name": "Country", "value": "morocco"},
    ],
}

form_element_field = {
    "id": "2",
    "name": "test",
    "form_element_fields": [
        {
            "id": "101",
            "form_element_template_id": "7",
            "form_id": "2",
            "form_element_template": {
                "id": "7",
                "name": "Gender",
                "form_element_type_id": "19",
                "form_element_type": {
                    "id": "19",
                    "name": "checkbox",
                },
                "form_element_options": [
                    {
                        "id": "12",
                        "form_element_template_id": "7",
                        "selected_value_id": "null",
                        "value": "male",
                    },
                    {
                        "id": "13",
                        "form_element_template_id": "7",
                        "selected_value_id": "null",
                        "value": "female",
                    },
                ],
            },
        },
        {
            "id": "102",
            "form_element_template_id": "8",
            "form_id": "2",
            "form_element_template": {
                "id": "8",
                "name": "Full name",
                "form_element_type_id": "20",
                "form_element_type": {
                    "id": "20",
                    "name": "text",
                    "form_element_template_id": "8",
                },
                "form_element_options": [],
            },
        },
    ],
}

selected_value_for_update = [
    {
        "id": "87",
        "form_element_template_id": "7",
        "client_id": "11",
        "value": "null",
        "selected_list_values": [
            {
                "id": "300",
                "form_element_options_id": "12",
                "selected_value_id": "87",
                "form_element_option": {
                    "id": "12",
                    "form_element_template_id": "7",
                    "value": "male",
                },
            }
        ],
        "form_element_template": {
            "id": "7",
            "name": "Gender",
            "form_element_type_id": "19",
            "form_element_type": {
                "id": "19",
                "name": "checkbox",
            },
            "form_element_options": [
                {
                    "id": "12",
                    "form_element_template_id": "7",
                    "selected_value_id": "null",
                    "value": "male",
                },
                {
                    "id": "13",
                    "form_element_template_id": "7",
                    "selected_value_id": "null",
                    "value": "female",
                },
            ],
        },
    },
    {
        "id": "82",
        "form_element_template_id": "8",
        "client_id": "11",
        "value": "jone doe",
        "selected_list_values": [],
        "form_element_template": {
            "id": "8",
            "name": "Full name",
            "form_element_type_id": "20",
            "form_element_type": {
                "id": "20",
                "name": "text",
            },
            "form_element_options": [],
        },
    },
]

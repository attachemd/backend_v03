collected_data = {
    "form_id": "2",
    "name": "Test",
    "form_elements": [
        {"name": "Full name", "value": "john doe"},
        {"name": "Gender", "value": "male"},
    ],
}

form_template = {
    "id": "2",
    "name": "test",
    "element_form_mtms": [
        {
            "id": "101",
            "form_element_id": "7",
            "form_id": "2",
            "form_element": {
                "id": "7",
                "name": "Gender",
                "form_element_type_id": "19",
                "form_element_type": {
                    "id": "19",
                    "name": "checkbox",
                },
                "form_element_list_values": [
                    {
                        "id": "12",
                        "form_element_id": "7",
                        "filled_form_id": "null",
                        "value": "male",
                    },
                    {
                        "id": "13",
                        "form_element_id": "7",
                        "filled_form_id": "null",
                        "value": "female",
                    },
                ],
            },
        },
        {
            "id": "102",
            "form_element_id": "8",
            "form_id": "2",
            "form_element": {
                "id": "8",
                "name": "Full name",
                "form_element_type_id": "20",
                "form_element_type": {
                    "id": "20",
                    "name": "text",
                    "form_element_id": "8",
                },
                "form_element_list_values": [],
            },
        },
    ],
}

filled_form_for_update = [
    {
        "id": "87",
        "form_element_id": "7",
        "value": "null",
        "list_value_filled_form_mtms": [
            {
                "id": "300",
                "form_element_list_values_id": "12",
                "filled_form_id": "87",
                "form_element_list_value": {
                    "id": "12",
                    "form_element_id": "7",
                    "value": "male",
                },
            }
        ],
        "form_element": {
            "id": "7",
            "name": "Gender",
            "form_element_type_id": "19",
            "form_element_type": {
                "id": "19",
                "name": "checkbox",
            },
            "form_element_list_values": [
                {
                    "id": "12",
                    "form_element_id": "7",
                    "filled_form_id": "null",
                    "value": "male",
                },
                {
                    "id": "13",
                    "form_element_id": "7",
                    "filled_form_id": "null",
                    "value": "female",
                },
            ],
        },
    },
    {
        "id": "82",
        "form_element_id": "8",
        "value": "jone doe",
        "list_value_filled_form_mtms": [],
        "form_element": {
            "id": "8",
            "name": "Full name",
            "form_element_type_id": "20",
            "form_element_type": {
                "id": "20",
                "name": "text",
            },
            "form_element_list_values": [],
        },
    },
]

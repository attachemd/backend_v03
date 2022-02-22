collected_data = {
    "form_id": "2",
    "name": "Test",
    "form_elements": [
        {"name": "Full name", "value": "john doe"},
        {"name": "Gender", "value": "male"},
    ],
}

form_element_list_value = [
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
]

# form element and form have many to many relationship

form = {
    "form": {
        "id": "2",
        "name": "test",
        "form_elements": [
            {
                "id": "7",
                "form_id": "2",
                "name": "Gender",
                "form_element_types": [
                    {
                        "id": "19",
                        "name": "checkbox",
                        "form_element_id": "7",
                    },
                ],
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
            {
                "id": "8",
                "form_id": "2",
                "name": "Full name",
                "form_element_types": [
                    {
                        "id": "20",
                        "name": "text",
                        "form_element_id": "8",
                    },
                ],
                "form_element_list_values": [],
            },
        ],
    },
}

new_form = {
    "form": {
        "id": "2",
        "name": "test",
        "form_elements": [
            {
                "id": "7",
                "form_id": "5",
                "name": "Gender",
                "form_element_types": [
                    {
                        "id": "19",
                        "name": "checkbox",
                        "form_element_id": "7",
                    },
                ],
                "filled_forms": [
                    {
                        "id": "87",
                        "form_element_id": "7",
                        "value": "null",
                        "form_element_list_values": [
                            {
                                "id": "12",
                                "form_element_id": "7",
                                "filled_form_id": "87",
                                "value": "male",
                                "form_element": {},
                            }
                        ],
                    },
                ],
            },
            {
                "id": "8",
                "form_id": "2",
                "name": "Full name",
                "form_element_types": [
                    {
                        "id": "20",
                        "name": "text",
                        "form_element_id": "8",
                    },
                ],
                "filled_forms": [
                    {
                        "id": "82",
                        "form_element_id": "8",
                        "value": "jone doe",
                        "form_element_list_values": [],
                    },
                ],
            },
        ],
    },
}

filled_form = [
    {
        "id": "87",
        "form_element_id": "7",
        "value": "null",
        "form_element_list_values": [
            {
                "id": "12",
                "form_element_id": "7",
                "filled_form_id": "87",
                "value": "male",
            },
        ],
        "form_element": {
            "id": "7",
            "form_id": "2",
            "name": "Gender",
        },
    },
    {
        "id": "82",
        "form_element_id": "8",
        "value": "jone doe",
        "form_element_list_values": [],
        "form_element": {
            "id": "8",
            "form_id": "2",
            "name": "Full name",
        },
    },
]


test01 = {
    "form": {"id": "2", "name": "test"},
    "form_element": {"id": "7", "form_id": "5", "name": "Gender"},
    "form_element_type": {
        "id": "19",
        "name": "checkbox",
        "form_element_id": "7",
    },
    "form_element_list_value": [
        {
            "id": "12",
            "form_element_id": "7",
            "value": "male",
            "form_element": {},
        },
        {
            "id": "13",
            "form_element_id": "7",
            "value": "female",
            "form_element": {},
        },
    ],
    "selected_form_element_list_values": [
        {
            "id": "15",
            "form_element_list_value_id": "12",
            "filled_form_id": "87",
        }
    ],
    "filled_form": {
        "id": "87",
        "form_element_id": "7",
        "value": "null",
    },
}

test02 = {
    "form": {"id": "2", "name": "test"},
    "form_element": {"id": "8", "form_id": "2", "name": "Full name"},
    "form_element_type": {
        "id": "20",
        "name": "text",
        "form_element_id": "8",
    },
    "form_element_list_value": [],
    "selected_form_element_list_value": [{}],
    "filled_form": {
        "id": "87",
        "form_element_id": "8",
        "value": "jone doe",
    },
}

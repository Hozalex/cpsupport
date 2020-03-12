class Company:
    def __init__(self, name, site="None", email="None", phone="None", address="None", comment="None", observer_ids=None,
                 default_assignee_id=0, category_code="None", additional_name="None"):
        if observer_ids is None:
            observer_ids = [0]
        self.name = name
        self.additional_name = additional_name
        self.site = site
        self.email = email
        self.phone = phone
        self.address = address
        self.comment = comment
        self.observer_ids = observer_ids
        self.default_assignee_id = default_assignee_id
        self.category_code = category_code
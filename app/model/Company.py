class Company:
    def __init__(self, name, additional_name, site, email, phone, address, comment, observer_ids, default_assignee_id,
                 category_code):
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

class NewModel(admin.ModelAdmin):

    def get_fields(self, request, obj):
        list = []
        sub = MyModel.objects.filter(parent_id=obj.entity_id)
        dico = obj.__dict__
        for i in sub:
            for j in dico:
                if i.tag == j:
                    list.append(j)
        return list
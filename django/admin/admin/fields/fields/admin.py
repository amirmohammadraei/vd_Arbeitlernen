class SampleModel(admin.ModelAdmin):
    fields = [('person', 'student_no', 'priority', 
            'status','major', 'level', 
            'system'), ('college', 'org1',
            'group', 'entry_term', 'entry_type',
            'last_term', 'is_active'), ]

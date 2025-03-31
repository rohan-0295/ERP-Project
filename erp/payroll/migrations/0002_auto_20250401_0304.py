from django.db import migrations

def create_trigger(apps, schema_editor):
    schema_editor.connection.cursor().execute("""
        CREATE TRIGGER update_net_salary
        BEFORE INSERT ON payroll_payroll
        FOR EACH ROW
        BEGIN
            DECLARE tax DECIMAL(10,2);
            DECLARE bonus DECIMAL(10,2);
            
            -- Calculate tax based on the tax_percentage from the Tax table
            SELECT tax_percentage INTO tax
            FROM payroll_tax
            WHERE employee_id = NEW.employee_id
            AND tax_date <= NEW.payment_date
            ORDER BY tax_date DESC
            LIMIT 1;

            -- Calculate bonus based on Bonus table for the employee
            SELECT IFNULL(SUM(amount), 0) INTO bonus
            FROM payroll_bonus
            WHERE employee_id = NEW.employee_id
            AND bonus_date <= NEW.payment_date;

            -- Set the net salary as gross_salary - tax and add bonus
            SET NEW.net_salary = NEW.gross_salary - (NEW.gross_salary * tax / 100) + bonus;
        END
    """)
    
class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_trigger),
    ]

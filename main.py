# ==========================================
# Rabea Calculator App
# Built with Kivy
# ==========================================


# -------------------------------
# استيراد المكتبات المطلوبة
# -------------------------------

from kivy.app import App

# BoxLayout لترتيب العناصر في صفوف وأعمدة
from kivy.uix.boxlayout import BoxLayout

# GridLayout لإنشاء شبكة أزرار الحاسبة
from kivy.uix.gridlayout import GridLayout

# Button لإنشاء الأزرار
from kivy.uix.button import Button

# Label لعرض النصوص والنتائج
from kivy.uix.label import Label

# Clock لتنفيذ شيء بعد وقت معين
from kivy.clock import Clock

# Window للتحكم في لون خلفية التطبيق
from kivy.core.window import Window

# dp لجعل أحجام العناصر مناسبة لمختلف الشاشات
from kivy.metrics import dp

# استيراد مكتبة الرياضيات
import math


# ==========================================
# إعدادات شكل التطبيق
# ==========================================

# جعل خلفية التطبيق سوداء
Window.clearcolor = (0, 0, 0, 1)


# ==========================================
# شاشة الترحيب
# ==========================================

class WelcomeScreen(BoxLayout):

    # دالة إنشاء شاشة الترحيب
    def __init__(self, app, **kwargs):

        # استدعاء الـ constructor الأساسي
        super().__init__(**kwargs)

        # حفظ التطبيق الأساسي
        self.app = app

        # جعل الشاشة في المنتصف
        self.orientation = "vertical"

        # إضافة مسافات من الأطراف
        self.padding = dp(20)

        # إنشاء مساحة فارغة فوق الرسالة
        top_space = Label()

        # إضافة المساحة للشاشة
        self.add_widget(top_space)

        # إنشاء رسالة الترحيب
        welcome = Label(
            text="Welcome to Rabea App",

            # حجم الخط
            font_size=dp(30),

            # جعل الخط Bold
            bold=True,

            # لون النص أبيض
            color=(1,0, 0 , 6),

            # جعل الرسالة في المنتصف
            halign="center",

            valign="middle"
        )

        # ضبط حجم النص
        welcome.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        # إضافة الرسالة
        self.add_widget(welcome)

        # إنشاء مساحة فارغة تحت الرسالة
        bottom_space = Label()

        # إضافة المساحة
        self.add_widget(bottom_space)

        # بعد 5 ثواني افتح الحاسبة
        Clock.schedule_once(self.open_calculator, 3)


    # ======================================
    # فتح الحاسبة بعد انتهاء الترحيب
    # ======================================

    def open_calculator(self, dt):

        # تغيير واجهة التطبيق إلى الحاسبة
        self.app.root.clear_widgets()

        # إنشاء الحاسبة
        calculator = Calculator()

        # وضع الحاسبة في التطبيق
        self.app.root.add_widget(calculator)


# ==========================================
# الحاسبة الرئيسية
# ==========================================

class Calculator(BoxLayout):

    # ======================================
    # إنشاء الحاسبة
    # ======================================

    def __init__(self, **kwargs):

        # استدعاء BoxLayout الأساسي
        super().__init__(**kwargs)

        # ترتيب العناصر رأسيًا
        self.orientation = "vertical"

        # المسافة الداخلية
        self.padding = dp(10)

        # المسافة بين العناصر
        self.spacing = dp(8)

        # تخزين العملية الحسابية الحالية
        self.expression = ""

        # تحديد الوضع الحالي
        # False = Basic
        # True = Scientific
        self.scientific_mode = False

        # إنشاء شاشة عرض العملية
        self.display = Label(
            text="",

            # حجم الخط
            font_size=dp(32),

            # محاذاة النص لليمين
            halign="right",

            valign="middle",

            # لون النص أبيض
            color=(1, 1, 1, 1),

            # خلفية الشاشة
            # سيتم رسمها عن طريق Canvas لاحقًا
        )

        # تحديد مساحة النص
        self.display.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        # إضافة شاشة العرض
        self.add_widget(self.display)


        # ==================================
        # زر التحويل بين Basic و Scientific
        # ==================================

        self.mode_button = Button(
            text="Scientific",

            # حجم الزر
            size_hint_y=None,

            height=dp(45),

            # لون الزر
            background_normal="",

            background_color=(0.15, 0.15, 0.15, 1)
        )

        # عند الضغط يتم تغيير الوضع
        self.mode_button.bind(
            on_press=self.toggle_mode
        )

        # إضافة الزر
        self.add_widget(self.mode_button)


        # ==================================
        # مكان أزرار الحاسبة
        # ==================================

        self.buttons_area = BoxLayout(
            orientation="vertical"
        )

        # إضافة منطقة الأزرار
        self.add_widget(self.buttons_area)

        # بناء الأزرار
        self.build_buttons()


    # ==========================================
    # إنشاء زر
    # ==========================================

    def create_button(
        self,
        text,
        callback=None,
        orange=False
    ):

        # إنشاء الزر
        button = Button(

            # النص الموجود على الزر
            text=text,

            # حجم الخط
            font_size=dp(22),

            # إزالة الخلفية الافتراضية
            background_normal="",

            # لون الزر
            background_color=(
                (1, 0.45, 0, 1)
                if orange
                else
                (0.12, 0.12, 0.12, 1)
            ),

            # لون النص
            color=(1, 1, 1, 1)
        )

        # إذا كان هناك Function
        if callback:

            # ربط الزر بالـ Function
            button.bind(on_press=callback)

        # إرجاع الزر
        return button


    # ==========================================
    # بناء أزرار الحاسبة
    # ==========================================

    def build_buttons(self):

        # حذف الأزرار القديمة
        self.buttons_area.clear_widgets()


        # ======================================
        # الوضع العادي Basic
        # ======================================

        if not self.scientific_mode:

            # إنشاء Grid
            grid = GridLayout(

                # 4 أعمدة
                cols=4,

                # المسافة بين الأزرار
                spacing=dp(5)
            )


            # ----------------------------------
            # الصف الأول
            # ----------------------------------

            grid.add_widget(
                self.create_button(
                    "AC",
                    self.clear
                )
            )

            grid.add_widget(
                self.create_button(
                    "⌫",
                    self.backspace
                )
            )

            grid.add_widget(
                self.create_button(
                    "%",
                    self.add_operator
                )
            )

            grid.add_widget(
                self.create_button(
                    "÷",
                    self.add_operator
                )
            )


            # ----------------------------------
            # الصف الثاني
            # ----------------------------------

            for value in ["7", "8", "9"]:

                grid.add_widget(
                    self.create_button(
                        value,
                        self.add_number
                    )
                )

            grid.add_widget(
                self.create_button(
                    "×",
                    self.add_operator
                )
            )


            # ----------------------------------
            # الصف الثالث
            # ----------------------------------

            for value in ["4", "5", "6"]:

                grid.add_widget(
                    self.create_button(
                        value,
                        self.add_number
                    )
                )

            grid.add_widget(
                self.create_button(
                    "-",
                    self.add_operator
                )
            )


            # ----------------------------------
            # الصف الرابع
            # ----------------------------------

            for value in ["1", "2", "3"]:

                grid.add_widget(
                    self.create_button(
                        value,
                        self.add_number
                    )
                )

            grid.add_widget(
                self.create_button(
                    "+",
                    self.add_operator
                )
            )


            # ----------------------------------
            # الصف الخامس
            # ----------------------------------

            grid.add_widget(
                self.create_button(
                    "00",
                    self.add_number
                )
            )

            grid.add_widget(
                self.create_button(
                    "0",
                    self.add_number
                )
            )

            grid.add_widget(
                self.create_button(
                    ".",
                    self.add_number
                )
            )

            # زر المساواة باللون البرتقالي
            grid.add_widget(
                self.create_button(
                    "=",
                    self.calculate,
                    orange=True
                )
            )


            # إضافة الشبكة للتطبيق
            self.buttons_area.add_widget(grid)


        # ======================================
        # الوضع العلمي Scientific
        # ======================================

        else:

            # إنشاء Grid بخمسة أعمدة
            grid = GridLayout(
                cols=5,
                spacing=dp(5)
            )


            # ----------------------------------
            # الدوال العلمية
            # ----------------------------------

            scientific_buttons = [

                "sin",
                "cos",
                "tan",
                "rad",
                "deg",

                "log",
                "ln",
                "(",
                ")",
                "inv",

                "!",
                "AC",
                "%",
                "⌫",
                "÷",

                "^",
                "7",
                "8",
                "9",
                "×",

                "√",
                "4",
                "5",
                "6",
                "-",

                "π",
                "1",
                "2",
                "3",
                "+",

                "e",
                "00",
                "0",
                ".",
                "="
            ]


            # إنشاء كل زر
            for value in scientific_buttons:

                # زر AC
                if value == "AC":

                    button = self.create_button(
                        value,
                        self.clear
                    )

                # زر Backspace
                elif value == "⌫":

                    button = self.create_button(
                        value,
                        self.backspace
                    )

                # زر =
                elif value == "=":

                    button = self.create_button(
                        value,
                        self.calculate,
                        orange=True
                    )

                # الأرقام
                elif value.isdigit():

                    button = self.create_button(
                        value,
                        self.add_number
                    )

                # باقي الأزرار
                else:

                    button = self.create_button(
                        value,
                        self.scientific_action
                    )

                # إضافة الزر
                grid.add_widget(button)


            # إضافة Grid
            self.buttons_area.add_widget(grid)


    # ==========================================
    # إضافة رقم
    # ==========================================

    def add_number(self, button):

        # إضافة الرقم إلى العملية
        self.expression += button.text

        # تحديث الشاشة
        self.display.text = self.expression


    # ==========================================
    # إضافة عملية حسابية
    # ==========================================

    def add_operator(self, button):

        # تحويل شكل العمليات إلى Python
        operator = button.text

        if operator == "×":
            operator = "*"

        elif operator == "÷":
            operator = "/"

        # إضافة العملية
        self.expression += operator

        # تحديث الشاشة
        self.display.text = self.expression


    # ==========================================
    # حذف كل شيء
    # ==========================================

    def clear(self, button):

        # تفريغ العملية
        self.expression = ""

        # تفريغ الشاشة
        self.display.text = ""


    # ==========================================
    # حذف آخر حرف
    # ==========================================

    def backspace(self, button):

        # حذف آخر حرف
        self.expression = self.expression[:-1]

        # تحديث الشاشة
        self.display.text = self.expression


    # ==========================================
    # العمليات العلمية
    # ==========================================

    def scientific_action(self, button):

        # معرفة الزر الذي تم الضغط عليه
        value = button.text


        # ----------------------------------
        # النسبة المئوية
        # ----------------------------------

        if value == "%":

            self.expression += "/100"


        # ----------------------------------
        # الضرب
        # ----------------------------------

        elif value == "×":

            self.expression += "*"


        # ----------------------------------
        # القسمة
        # ----------------------------------

        elif value == "÷":

            self.expression += "/"


        # ----------------------------------
        # الجمع والطرح
        # ----------------------------------

        elif value in ["+", "-"]:

            self.expression += value


        # ----------------------------------
        # الأس
        # ----------------------------------

        elif value == "^":

            self.expression += "**"


        # ----------------------------------
        # الجذر التربيعي
        # ----------------------------------

        elif value == "√":

            self.expression += "sqrt("


        # ----------------------------------
        # π
        # ----------------------------------

        elif value == "π":

            self.expression += "pi"


        # ----------------------------------
        # e
        # ----------------------------------

        elif value == "e":

            self.expression += "e"


        # ----------------------------------
        # فتح قوس
        # ----------------------------------

        elif value == "(":

            self.expression += "("


        # ----------------------------------
        # قفل قوس
        # ----------------------------------

        elif value == ")":

            self.expression += ")"


        # ----------------------------------
        # sin
        # ----------------------------------

        elif value == "sin":

            self.expression += "sin("


        # ----------------------------------
        # cos
        # ----------------------------------

        elif value == "cos":

            self.expression += "cos("


        # ----------------------------------
        # tan
        # ----------------------------------

        elif value == "tan":

            self.expression += "tan("


        # ----------------------------------
        # log
        # ----------------------------------

        elif value == "log":

            self.expression += "log10("


        # ----------------------------------
        # ln
        # ----------------------------------

        elif value == "ln":

            self.expression += "log("


        # ----------------------------------
        # factorial
        # ----------------------------------

        elif value == "!":

            self.expression += "factorial("


        # ----------------------------------
        # تحديث الشاشة
        # ----------------------------------

        self.display.text = self.expression


    # ==========================================
    # تنفيذ العملية الحسابية
    # ==========================================

    def calculate(self, button):

        # التأكد أن الشاشة ليست فارغة
        if not self.expression:

            return

        try:

            # ----------------------------------
            # الدوال الآمنة التي يسمح بها eval
            # ----------------------------------

            safe_functions = {

                "sin": lambda x:
                math.sin(math.radians(x)),

                "cos": lambda x:
                math.cos(math.radians(x)),

                "tan": lambda x:
                math.tan(math.radians(x)),

                "sqrt": math.sqrt,

                "log10": math.log10,

                "log": math.log,

                "factorial": math.factorial,

                "pi": math.pi,

                "e": math.e
            }


            # ----------------------------------
            # تنفيذ العملية
            # ----------------------------------

            result = eval(
                self.expression,
                {
                    "__builtins__": {}
                },
                safe_functions
            )


            # ----------------------------------
            # إزالة .0 من الأرقام الصحيحة
            # ----------------------------------

            if isinstance(result, float) and result.is_integer():

                result = int(result)


            # ----------------------------------
            # عرض النتيجة
            # ----------------------------------

            self.display.text = str(result)

            # جعل النتيجة هي العملية الحالية
            self.expression = str(result)


        # ----------------------------------
        # لو حصل خطأ في الحساب
        # ----------------------------------

        except ZeroDivisionError:

            self.display.text = "Cannot divide by zero"

            self.expression = ""


        # ----------------------------------
        # لو العملية غير صحيحة
        # ----------------------------------

        except Exception:

            self.display.text = "Error"

            self.expression = ""


    # ==========================================
    # التحويل بين Basic و Scientific
    # ==========================================

    def toggle_mode(self, button):

        # عكس الوضع الحالي
        self.scientific_mode = not self.scientific_mode

        # تغيير اسم الزر
        if self.scientific_mode:

            self.mode_button.text = "Basic"

        else:

            self.mode_button.text = "Scientific"


        # إعادة بناء الأزرار
        self.build_buttons()


# ==========================================
# تشغيل التطبيق
# ==========================================

class RabeaApp(App):

    # ======================================
    # بناء التطبيق
    # ======================================

    def build(self):

        # إنشاء Root Layout
        root = BoxLayout(
            orientation="vertical"
        )

        # إضافة شاشة الترحيب
        root.add_widget(
            WelcomeScreen(self)
        )

        # إرجاع الواجهة
        return root


# ==========================================
# تشغيل البرنامج
# ==========================================

if __name__ == "__main__":

    # تشغيل التطبيق
    RabeaApp().run()

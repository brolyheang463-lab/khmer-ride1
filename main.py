from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

Window.size = (360, 640)

class KhmerRideApp(App):
    def build(self):
        self.title = "Khmer Ride - កក់ការធ្វើដំណើរ"
        
        root = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        with root.canvas.before:
            Color(0.12, 0.05, 0.05, 1)
            self.rect = Rectangle(size=Window.size, pos=root.pos)
        root.bind(size=self._update_rect, pos=self._update_rect)

        title_layout = BoxLayout(orientation='vertical', size_hint_y=0.25, spacing=5)
        
        app_title = Label(
            text="🇰🇭 ហ្វឺស-រ៉ាយ (Khmer Ride)", 
            font_size=24, 
            bold=True, 
            color=(1, 0.84, 0, 1)
        )
        app_subtitle = Label(
            text="សេវាកម្មធ្វើដំណើររហ័ស ទាន់ចិត្ត សុវត្ថិភាព", 
            font_size=13, 
            color=(0.9, 0.9, 0.9, 1)
        )
        title_layout.add_widget(app_title)
        title_layout.add_widget(app_subtitle)
        root.add_widget(title_layout)

        form_layout = GridLayout(cols=1, spacing=12, size_hint_y=0.45)

        self.pickup_input = TextInput(
            hint_text='📍 ទីតាំងត្រូវទទួល (Pickup Location)',
            multiline=False,
            font_size=14,
            size_hint_y=None,
            height=45
        )
        
        self.dest_input = TextInput(
            hint_text='🏁 ទីតាំងទិសដៅ (Destination)',
            multiline=False,
            font_size=14,
            size_hint_y=None,
            height=45
        )

        self.distance_input = TextInput(
            hint_text='🛣️ ចម្ងាយทาง (គីឡូម៉ែត្រ)',
            multiline=False,
            input_filter='float',
            font_size=14,
            size_hint_y=None,
            height=45
        )

        form_layout.add_widget(self.pickup_input)
        form_layout.add_widget(self.dest_input)
        form_layout.add_widget(self.distance_input)
        root.add_widget(form_layout)

        btn_layout = BoxLayout(size_hint_y=0.15, padding=[0, 5])
        self.book_btn = Button(
            text='🛺 គណនាថ្លៃឈ្នួល និងកក់ឥឡូវនេះ',
            font_size=16,
            bold=True,
            background_color=(1, 0.75, 0, 1),
            color=(0.1, 0.1, 0.1, 1)
        )
        self.book_btn.bind(on_press=self.calculate_fare)
        btn_layout.add_widget(self.book_btn)
        root.add_widget(btn_layout)

        self.result_label = Label(
            text="✨ សូមបញ្ចូលចម្ងាយដើម្បីគណនាតម្លៃ ✨",
            font_size=15,
            bold=True,
            color=(1, 1, 1, 1),
            size_hint_y=0.15
        )
        root.add_widget(self.result_label)

        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def calculate_fare(self, instance):
        try:
            distance_text = self.distance_input.text.strip()
            if not distance_text:
                self.result_label.text = "⚠️ សូមបំពេញចម្ងាយជាគីឡូម៉ែត្រជាមុនសិន!"
                return
            
            dist = float(distance_text)
            
            if dist <= 5:
                fare = dist * 3000
                rate_info = "(អត្រា ៣,០០០រៀល/គម ក្រោម ៥គម)"
            else:
                fare = dist * 2000
                rate_info = "(អត្រា ២,០០0រៀល/គម លើស ៥គម)"
            
            self.result_label.text = f"💰 តម្លៃសរុប: {fare:,.0f} រៀល\n{rate_info}"
        
        except ValueError:
            self.result_label.text = "❌ សូមបញ្ចូលលេខចម្ងាយឱ្យបានត្រឹមត្រូវ!"

if __name__ == '__main__':
    KhmerRideApp().run()
      

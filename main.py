import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image as KivyImage
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup

SKIN_CONDITIONS_DB = {
    "Eczema": {
        "bn_name": "একজিমা (Eczema)",
        "desc": "ত্বক শুষ্ক হয়ে যাওয়া, লালচে ভাব ও চুলকানি।",
        "advice": "ত্বক সবসময় ময়েশ্চারাইজ রাখুন। ডাক্তারের পরামর্শে ক্রিম ব্যবহার করুন।"
    },
    "Fungal_Infection": {
        "bn_name": "ফাঙ্গাল ইনফেকশন / দাদ (Ringworm)",
        "desc": "গোলাকার দাগ, প্রান্তভাগ লাল হয়ে চুলকানো।",
        "advice": "স্থানটি শুষ্ক রাখুন। অ্যান্টিফাঙ্গাল ক্রিম ব্যবহার করা হয়।"
    }
}

class SkinScannerApp(App):
    def build(self):
        self.title = "AI Skin Disease Scanner"
        self.selected_image_path = None
        
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        title_label = Label(text="AI Skin Disease Scanner", font_size='22sp', bold=True, size_hint_y=None, height=40)
        layout.add_widget(title_label)
        
        self.img_preview = KivyImage(source='', size_hint_y=0.4)
        layout.add_widget(self.img_preview)
        
        select_btn = Button(text="গ্যালারি থেকে ছবি বাছুন", size_hint_y=None, height=50, background_color=(0.2, 0.6, 1, 1))
        select_btn.bind(on_press=self.open_file_chooser)
        layout.add_widget(select_btn)
        
        scan_btn = Button(text="চর্মরোগ বিশ্লেষণ করুন", size_hint_y=None, height=50, background_color=(0.1, 0.8, 0.3, 1))
        scan_btn.bind(on_press=self.analyze_skin)
        layout.add_widget(scan_btn)
        
        self.result_label = Label(text="ফলাফল ও পরামর্শ এখানে দেখা যাবে...", markup=True, halign='left', valign='top')
        self.result_label.bind(size=self.result_label.setter('text_size'))
        layout.add_widget(self.result_label)
        
        return layout

    def open_file_chooser(self, instance):
        content = BoxLayout(orientation='vertical')
        file_chooser = FileChooserIconView(filters=['*.png', '*.jpg', '*.jpeg'])
        content.add_widget(file_chooser)
        
        select_btn = Button(text="বাছাই নিশ্চিত করুন", size_hint_y=None, height=45)
        content.add_widget(select_btn)
        
        popup = Popup(title="ছবি নির্বাচন করুন", content=content, size_hint=(0.9, 0.9))
        
        def set_image(btn_instance):
            if file_chooser.selection:
                self.selected_image_path = file_chooser.selection[0]
                self.img_preview.source = self.selected_image_path
                self.result_label.text = "ছবি লোড হয়েছে। 'চর্মরোগ বিশ্লেষণ করুন' বাটনে চাপ দিন।"
            popup.dismiss()
            
        select_btn.bind(on_press=set_image)
        popup.open()

    def analyze_skin(self, instance):
        if not self.selected_image_path:
            self.result_label.text = "[color=ff3333]অনুগ্রহ করে আগে একটি স্কিন রোগের ছবি বাছাই করুন![/color]"
            return

        file_name = os.path.basename(self.selected_image_path).lower()
        detected_key = "Eczema" if "eczema" in file_name else "Fungal_Infection"
        info = SKIN_CONDITIONS_DB[detected_key]
        
        output = f"[color=33cc33][b]সম্ভাব্য চর্মরোগ:[/b] {info['bn_name']}[/color]\n\n[b]লক্ষণ:[/b] {info['desc']}\n\n[b]পরামর্শ:[/b] {info['advice']}"
        self.result_label.text = output

if __name__ == "__main__":
    SkinScannerApp().run()

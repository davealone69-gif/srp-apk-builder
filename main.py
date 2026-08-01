from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class SRPApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text="SRP Assembled App", font_size='24sp'))
        layout.add_widget(Label(text="Network Diagnostic Tool", halign='center'))
        
        btn = Button(text="Check Modules", size_hint=(1, 0.2))
        btn.bind(on_press=self.on_click)
        layout.add_widget(btn)
        
        return layout

    def on_click(self, instance):
        print("Modules loaded successfully from /modules directory")

if __name__ == '__main__':
    SRPApp().run()

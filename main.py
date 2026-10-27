from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import datetime, json, os

NOTA_PATH = '/sdcard/Download/launcher_nota.json'

class Launcher(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(orientation='vertical', padding=15, spacing=10, **kwargs)
        
        # 1. RELOJ 58
        self.reloj = Label(text='', font_size=58, size_hint_y=0.25, color=(1,1,1,1), bold=True)
        self.add_widget(self.reloj)
        Clock.schedule_interval(self.update_reloj, 1)
        self.update_reloj(0)

        # 2. NOTA GRIS #2A2A2A
        from kivy.uix.floatlayout import FloatLayout
        from kivy.graphics import Color, RoundedRectangle
        f = FloatLayout(size_hint_y=0.35)
        with f.canvas.before:
            Color(0.164,0.164,0.164,1) # #2A2A2A
            self.rect = RoundedRectangle(radius=[15], size=f.size, pos=f.pos)
        f.bind(size=self._upd_rect, pos=self._upd_rect)
        
        self.nota = Label(text=self.cargar_nota(), font_size=17, halign='left', valign='top', color=(1,1,1,1))
        self.nota.bind(size=lambda *a: setattr(self.nota, 'text_size', (self.nota.width-20, None)))
        f.add_widget(self.nota)
        self.add_widget(f)

        # 3. 4 APPS FIJAS
        g = GridLayout(cols=2, spacing=12, size_hint_y=0.25)
        g.add_widget(Button(text='WhatsApp', on_press=lambda x: self.abrir_app('com.whatsapp')))
        g.add_widget(Button(text='Llamadas', on_press=lambda x: self.abrir_app('com.android.dialer')))
        g.add_widget(Button(text='Camara', on_press=lambda x: self.abrir_app('com.android.camera2')))
        g.add_widget(Button(text='Netflix', on_press=lambda x: self.abrir_app('com.netflix.mediaclient')))
        self.add_widget(g)

        # 4. BOTON CAJON
        self.add_widget(Button(text='▲ TODAS LAS APPS ▲', size_hint_y=0.15, background_color=(0.2,0.2,0.2,1), on_press=self.mostrar_apps))

        # Cajon escondido
        self.scroll = ScrollView(size_hint=(1,1))
        self.apps_grid = GridLayout(cols=1, spacing=
      

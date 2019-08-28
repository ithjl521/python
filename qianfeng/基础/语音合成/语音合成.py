import win32com.client

dehua = win32com.client.Dispatch('API.APVOICE')

dehua.Speak('123')
def mood_response(mood):
   if mood.lower() == "happy":
      return "Good too hear!"
   elif mood.lower() == "sad":
      return "Im sorry too hear that"
   elif mood.lower() == "excited":
      return "Im glad you're excited!"
   elif mood.lower() == "scared":
      return "Dont be scared!"
   else:
     return "Sorry I dont understand your mood"
from booking.booking import Booking 

with Booking(teardown= True) as bot:

    try:

        bot.land_the_first_page()
 
        
    except Exception as e:
        if 'in PATH' in str(e):
            print(
                'You are trying to run the bot from command line \n'
                'Please add to PATH your Selenium Drivers \n'
                'Windows: \n'
                '    set PATH=%PATH%;C:path-to-your-folder \n \n'
                'Linux: \n'
                '    PATH=$PATH:/path/toyour/folder/ \n'
            )
        else:
            raise
    
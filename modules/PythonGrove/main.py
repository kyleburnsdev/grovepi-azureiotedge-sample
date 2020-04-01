import time
import os
import sys
import asyncio
from six.moves import input
import threading
import grovepi

async def main():
    try:
        if not sys.version >= "3.5.3":
            raise Exception( "The sample requires python 3.5.3+. Current version of Python: %s" % sys.version )
        print ( "GROVEIOT: Running main" )

        stopFlag = threading.Event()

        # define behavior for receiving an input message on input1
        async def processing_loop():
            LED_BAR_PORT = 5 #D5
            counter = 0

            print("GROVEIOT: setting up device communication")
            grovepi.pinMode(LED_BAR_PORT, "OUTPUT")
            time.sleep(1)
            print("GROVEIOT: initializing device")
            grovepi.ledBar_init(LED_BAR_PORT, counter)
            time.sleep(.1)

            print("GROVEIOT: entering processing loop")
            while not stopFlag.isSet():
                counter = counter + 1
                grovepi.ledBar_setLevel(LED_BAR_PORT, counter % 10)
                time.sleep(1)

            # we're done, turn off the lights
            grovepi.ledBar_setLevel(LED_BAR_PORT, 0)

        # define behavior for halting the application
        def stdin_listener():
            while True:
                try:
                    selection = input("Press Q to quit\n")
                    if selection == "Q" or selection == "q":
                        stopFlag.set()
                        print("Quitting...")
                        break
                except:
                    time.sleep(10)

        # Schedule the main processing loop
        listeners = asyncio.gather(processing_loop())

        print ( "GROVEPI: initiated processing loop")

        # Run the stdin listener in the event loop
        loop = asyncio.get_event_loop()
        user_finished = loop.run_in_executor(None, stdin_listener)

        # Wait for user to indicate they are done listening for messages
        await user_finished

        # Cancel listening
        listeners.cancel()

    except Exception as e:
        print ( "Unexpected error %s " % e )
        raise

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
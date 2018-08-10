from lib.common.token_obfuscators import *
from lib.common.command_obfuscators import *
from lib.common.helpers import RandomGen, choosePrefObfuscator


class ObfuscationHandler(object):
    """
    Manages command and script obfuscation. Obfuscates based off of 
    the user's set options
    """
    def __init__(self, tokObfuscators, cmdObfuscators, args):
        self.tokObfuscators = tokObfuscators
        self.cmdObfuscators = cmdObfuscators
        self.layers = args.layers
        self.sizePref = args.payload_size
        self.timePref = args.execution_time
        self.binaryPref = args.binaryPref

        if args.command:
            self.originalCmd = args.command
        else:
            self.originalCmd = args.file.read()

    def generatePayload(self):
        payload = self.originalCmd

        for i in range(self.layers):
            tokObfuscator = choosePrefObfuscator(self.tokObfuscators, self.sizePref)
            cmdObfuscator = choosePrefObfuscator(self.cmdObfuscators, self.sizePref, self.timePref, self.binaryPref)

            payload = cmdObfuscator.obfuscate(self.sizePref, self.timePref, self.binaryPref, payload)
            #obCmd = tokObfuscator.obfuscate(self.sizePref, obCmd)

        return payload

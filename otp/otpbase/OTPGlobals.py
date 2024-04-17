from panda3d.core import *

QuietZone = 1
UberZone = 2
WallBitmask = BitMask32(1)
FloorBitmask = BitMask32(2)
CameraBitmask = BitMask32(4)
CameraTransparentBitmask = BitMask32(8)
SafetyNetBitmask = BitMask32(512)
SafetyGateBitmask = BitMask32(1024)
GhostBitmask = BitMask32(2048)
PathFindingBitmask = BitMask32.bit(29)
OriginalCameraFov = 52.0
DefaultCameraFov = 52.0
DefaultCameraFar = 400.0
DefaultCameraNear = 1.0
AICollisionPriority = 10
AICollMovePriority = 8
MaxFriends = 50
MaxPlayerFriends = 300
MaxBackCatalog = 48
FriendChat = 1
CommonChat = 1
SuperChat = 2
MaxCustomMessages = 25
SPInvalid = 0
SPHidden = 1
SPRender = 2
SPDynamic = 5
CENormal = 0
CEBigHead = 1
CESmallHead = 2
CEBigLegs = 3
CESmallLegs = 4
CEBigToon = 5
CESmallToon = 6
CEFlatPortrait = 7
CEFlatProfile = 8
CETransparent = 9
CENoColor = 10
CEInvisible = 11
CEPumpkin = 12
CEBigWhite = 13
CESnowMan = 14
CEGreenToon = 15
CEGhost = 'g'
BigToonScale = 1.5
SmallToonScale = 0.5
DisconnectUnknown = 0
DisconnectBookExit = 1
DisconnectCloseWindow = 2
DisconnectPythonError = 3
DisconnectSwitchShards = 4
DisconnectGraphicsError = 5
DisconnectReasons = {DisconnectUnknown: 'unknown',
 DisconnectBookExit: 'book exit',
 DisconnectCloseWindow: 'closed window',
 DisconnectPythonError: 'python error',
 DisconnectSwitchShards: 'switch shards',
 DisconnectGraphicsError: 'graphics error'}
DatabaseDialogTimeout = 20.0
DatabaseGiveupTimeout = 45.0
PeriodTimerWarningTime = (600, 300, 60)
WalkCutOff = 0.5
RunCutOff = 8.0
FloorOffset = 0.025
AvatarDefaultRadius = 1
InterfaceFont = None
InterfaceFontPath = None
SignFont = None
SignFontPath = None
FancyFont = None
FancyFontPath = None
NametagFonts = {}
NametagFontPaths = {}
DialogClass = None
GlobalDialogClass = None
ProductPrefix = None

def getInterfaceFont():
    global InterfaceFontPath
    global InterfaceFont
    if InterfaceFont == None:
        if InterfaceFontPath == None:
            InterfaceFont = TextNode.getDefaultFont()
        else:
            InterfaceFont = loader.loadFont(InterfaceFontPath, lineHeight=1.0)
    return InterfaceFont


def setInterfaceFont(path):
    global InterfaceFontPath
    global InterfaceFont
    InterfaceFontPath = path
    InterfaceFont = None
    return


def getSignFont():
    global SignFont
    global SignFontPath
    if SignFont == None:
        if SignFontPath == None:
            InterfaceFont = TextNode.getDefaultFont()
            SignFont = TextNode.getDefaultFont()
        else:
            SignFont = loader.loadFont(SignFontPath, lineHeight=1.0)
    return SignFont


def setSignFont(path):
    global SignFontPath
    SignFontPath = path


def getFancyFont():
    global FancyFontPath
    global FancyFont
    if FancyFont == None:
        if FancyFontPath == None:
            InterfaceFont = TextNode.getDefaultFont()
            FancyFont = TextNode.getDefaultFont()
        else:
            FancyFont = loader.loadFont(FancyFontPath, lineHeight=1.0)
    return FancyFont


def setFancyFont(path):
    global FancyFontPath
    FancyFontPath = path


def getNametagFont(index):
    global NametagFontPaths
    global NametagFonts
    if index not in NametagFonts or NametagFonts[index] == None:
        if index not in NametagFontPaths or NametagFontPaths[index] == None:
            InterfaceFont = TextNode.getDefaultFont()
            NametagFonts[index] = TextNode.getDefaultFont()
        else:
            NametagFonts[index] = loader.loadFont(NametagFontPaths[index], lineHeight=1.0)
    return NametagFonts[index]


def setNametagFont(index, path):
    NametagFontPaths[index] = path


def getDialogClass():
    global DialogClass
    if DialogClass == None:
        from otp.otpgui.OTPDialog import OTPDialog
        DialogClass = OTPDialog
    return DialogClass


def getGlobalDialogClass():
    global GlobalDialogClass
    if DialogClass == None:
        from otp.otpgui.OTPDialog import GlobalDialog
        GlobalDialogClass = GlobalDialog
    return GlobalDialogClass


def setDialogClasses(dialogClass, globalDialogClass):
    global DialogClass
    global GlobalDialogClass
    DialogClass = dialogClass
    GlobalDialogClass = globalDialogClass


def getDefaultProductPrefix():
    global ProductPrefix
    return ProductPrefix


def setDefaultProductPrefix(prefix):
    global ProductPrefix
    ProductPrefix = prefix


NetworkLatency = 1.0
maxLoginWidth = 9.1
STAND_INDEX = 0
WALK_INDEX = 1
RUN_INDEX = 2
REVERSE_INDEX = 3
STRAFE_LEFT_INDEX = 4
STRAFE_RIGHT_INDEX = 5
ToonStandableGround = 0.707
ToonSpeedFactor = 1.25
ToonForwardSpeed = 20.8
ToonJumpForce = 24.0
ToonReverseSpeed = 8.4 * ToonSpeedFactor
ToonRotateSpeed = 93.6
ToonRotateSprintingSpeed = 60 * ToonSpeedFactor
ToonForwardSlowSpeed = 6.0
ToonJumpSlowForce = 4.0
ToonReverseSlowSpeed = 2.5
ToonRotateSlowSpeed = 33.0
ToonDoubleTapSprintWindow = 0.40  # Time in seconds you have to register a double tap to turn on sprint mode
ToonSprintFovIncrease = 5  # How big should the fov increase when sprinting?
ToonForwardSprintSpeed = 20.16 * ToonSpeedFactor
ToonReverseSprintSpeed = 15 * ToonSpeedFactor
MickeySpeed = 5.0
MinnieSpeed = 3.2
DonaldSpeed = 3.68
GoofySpeed = 5.2
PlutoSpeed = 5.5
ThinkPosHotkey = 'shift-f1'
PlaceMarkerHotkey = 'f2'
FriendsListHotkey = 'f7'
StickerBookHotkey = 'f8'
OptionsPageHotkey = 'escape'
ScreenshotHotkey = 'f9'
SynchronizeHotkey = 'shift-f6'
QuestsHotkeyOn = 'end'
QuestsHotkeyOff = 'end-up'
InventoryHotkeyOn = 'home'
InventoryHotkeyOff = 'home-up'
MapHotkeyOn = 'delete'
MapHotkeyOff = 'delete-up'
DetectGarbageHotkey = 'shift-f11'
PrintCamPosHotkey = 'f12'
GlobalDialogColor = (1,
 1,
 0.75,
 1)
DefaultBackgroundColor = (0.3,
 0.3,
 0.3,
 1)
toonBodyScales = {'mouse': 0.6,
 'cat': 0.73,
 'duck': 0.66,
 'chicken': 0.66,
 'rabbit': 0.74,
 'horse': 0.85,
 'dog': 0.85,
 'monkey': 0.68,
 'bear': 0.85,
 'pig': 0.77}
toonHeadScales = {'mouse': Point3(1.0),
 'cat': Point3(1.0),
 'duck': Point3(1.0),
 'chicken': Point3(1.0),
 'rabbit': Point3(1.0),
 'horse': Point3(1.0),
 'dog': Point3(1.0),
 'monkey': Point3(1.0),
 'bear': Point3(1.0),
 'pig': Point3(1.0)}
legHeightDict = {'s': 1.5,
 'm': 2.0,
 'l': 2.75}
torsoHeightDict = {'s': 1.5,
 'm': 1.75,
 'l': 2.25,
 'ss': 1.5,
 'ms': 1.75,
 'ls': 2.25,
 'sd': 1.5,
 'md': 1.75,
 'ld': 2.25}
headHeightDict = {'dls': 0.75,
 'dss': 0.5,
 'dsl': 0.5,
 'dll': 0.75,
 'cls': 0.75,
 'css': 0.5,
 'csl': 0.5,
 'cll': 0.75,
 'hls': 0.75,
 'hss': 0.5,
 'hsl': 0.5,
 'hll': 0.75,
 'mls': 0.75,
 'mss': 0.5,
 'rls': 0.75,
 'rss': 0.5,
 'rsl': 0.5,
 'rll': 0.75,
 'fls': 0.75,
 'fss': 0.5,
 'fsl': 0.5,
 'fll': 0.75,
 'kss': 0.5,
 'ksl': 0.5,
 'kls': 0.5,
 'kll': 0.75,
 'pls': 0.75,
 'pss': 0.5,
 'psl': 0.5,
 'pll': 0.75,
 'bls': 0.75,
 'bss': 0.5,
 'bsl': 0.5,
 'bll': 0.75,
 'sls': 0.75,
 'sss': 0.5,
 'ssl': 0.5,
 'sll': 0.75}
RandomButton = 'Randomize'
TypeANameButton = 'Type Name'
PickANameButton = 'Pick-A-Name'
NameShopSubmitButton = 'Submit'
RejectNameText = 'That name is not allowed. Please try again.'
WaitingForNameSubmission = 'Submitting your name...'
NameShopNameMaster = 'NameMasterEnglish.txt'
NameShopPay = 'Subscribe Now!'
NameShopPlay = 'Free Trial'
NameShopOnlyPaid = 'Only paid users\nmay name their Toons.\nUntil you subscribe\nyour name will be\n'
NameShopContinueSubmission = 'Continue Submission'
NameShopChooseAnother = 'Choose Another Name'
NameShopToonCouncil = 'Your name\nwill be accepted\non next login.  \n' + 'Please re-log to\nget access to\nyour new name\nafter toon creation.'
PleaseTypeName = 'Please type your name:'
AllNewNames = 'All new names\nmust be approved\nby the Toon Council.'
NameShopNameRejected = 'The name you\nsubmitted has\nbeen rejected.'
NameShopNameAccepted = 'Congratulations!\nThe name you\nsubmitted has\nbeen accepted!'
NoPunctuation = "You can't use punctuation marks in your name!"
PeriodOnlyAfterLetter = 'You can use a period in your name, but only after a letter.'
ApostropheOnlyAfterLetter = 'You can use an apostrophe in your name, but only after a letter.'
NoNumbersInTheMiddle = 'Numeric digits may not appear in the middle of a word.'
ThreeWordsOrLess = 'Your name must be three words or fewer.'
CopyrightedNames = ('mickey',
 'mickey mouse',
 'mickeymouse',
 'minnie',
 'minnie mouse',
 'minniemouse',
 'donald',
 'donald duck',
 'donaldduck',
 'pluto',
 'goofy')
GuildUpdateMembersEvent = 'guildUpdateMembersEvent'
GuildInvitationEvent = 'guildInvitationEvent'
GuildAcceptInviteEvent = 'guildAcceptInviteEvent'
GuildRejectInviteEvent = 'guildRejectInviteEvent'
AvatarFriendAddEvent = 'avatarFriendAddEvent'
AvatarNewFriendAddEvent = 'avatarNewFriendAddEvent'
AvatarFriendUpdateEvent = 'avatarFriendUpdateEvent'
AvatarFriendRemoveEvent = 'avatarFriendRemoveEvent'
PlayerFriendAddEvent = 'playerFriendAddEvent'
PlayerFriendUpdateEvent = 'playerFriendUpdateEvent'
PlayerFriendRemoveEvent = 'playerFriendRemoveEvent'
AvatarFriendConsideringEvent = 'avatarFriendConsideringEvent'
AvatarFriendInvitationEvent = 'avatarFriendInvitationEvent'
AvatarFriendRejectInviteEvent = 'avatarFriendRejectInviteEvent'
AvatarFriendRetractInviteEvent = 'avatarFriendRetractInviteEvent'
AvatarFriendRejectRemoveEvent = 'avatarFriendRejectRemoveEvent'
PlayerFriendInvitationEvent = 'playerFriendInvitationEvent'
PlayerFriendRejectInviteEvent = 'playerFriendRejectInviteEvent'
PlayerFriendRetractInviteEvent = 'playerFriendRetractInviteEvent'
PlayerFriendRejectRemoveEvent = 'playerFriendRejectRemoveEvent'
PlayerFriendNewSecretEvent = 'playerFriendNewSecretEvent'
PlayerFriendRejectNewSecretEvent = 'playerFriendRejectNewSecretEvent'
PlayerFriendRejectUseSecretEvent = 'playerFriendRejectUseSecretEvent'
WhisperIncomingEvent = 'whisperIncomingEvent'
ChatFeedback_PassedBlacklist = 32
ChatFeedback_Whitelist = 64
ChatFeedback_OpenChat = 128
AccessUnknown = 0
AccessVelvetRope = 1
AccessFull = 2
AccessInvalid = 3
AvatarPendingCreate = -1
AvatarSlotUnavailable = -2
AvatarSlotAvailable = -3
accessLevelValues = {'NO_ACCESS': 0,
 'USER': 100,
 'MODERATOR': 200,
 'ADMIN': 300,
 'SYSTEM_ADMIN': 400,
 'SERVER_HOSTER': 500,
 'TTOFF_MODERATOR': 600,
 'TTOFF_CREATIVE_TEAM': 700,
 'TTOFF_DEVELOPER': 800}

BootedUnexpectedProblem = 1
BootedLoggedInElsewhere = 100
BootedKeyboardChatAuth = 120 # If I remember correctly, this is a bogus error message for hackers, but it doesn't seem to be used in TTOff
BootedConnectionKilled = 122 # GSM issues this when it enters the "Kill" state
BootedVersionMismatch = 124
BootedFileMismatch = 125
BootedNoAdminPrivileges = 126
BootedToonIssue = 127 # ???
BootedKickedForMaintenance = 151
BootedBanned = 152
BootedDistrictReset = 153
BootedOutOfTime = 288
BootedMoreInfo = [BootedUnexpectedProblem, BootedConnectionKilled, BootedToonIssue]
BootedNoReconnect = [BootedToonIssue, BootedBanned]
AccessLevelName2Int = {
 'RESTRICTED': -100,  # A user that has been banned, or is restricted in some manner
 'NO_ACCESS': 0,  # A user without access to commands
 'USER': 100,  # A user with access to most commands
 'BUILDER': 101, # A user with access to most commands, with additional access to SpawnProp features
 'MODERATOR': 200,  # A user with access to all commands
 'ADMIN': 300,  # A user with higher access level than previous
 'SYSTEM_ADMIN': 400,  # A user with higher access level than previous
 'SERVER_HOSTER': 500,  # The highest access level a normal player can obtain
 'TTOFF_CREATIVE_TEAM': 600,  # A Toontown Online Creative Team member
 'TTOFF_MODERATOR': 700,  # A Toontown Online Support Team member
 'TTOFF_DEVELOPER': 800  # A Toontown Online Developer
}
AccessLevelInt2Name = {
 -100: 'RESTRICTED',
 0: 'NO_ACCESS',
 100: 'USER',
 101: 'BUILDER',
 200: 'MODERATOR',
 300: 'ADMIN',
 400: 'SYSTEM_ADMIN',
 500: 'SERVER_HOSTER',
 600: 'TTOFF_CREATIVE_TEAM',
 700: 'TTOFF_MODERATOR',
 800: 'TTOFF_DEVELOPER'
}

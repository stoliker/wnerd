#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: WrestlingNerd.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxWindows' modules
from wxPython.wx import *

# Custom source
ID_DELETE_MATCH_MENU = wxNewId()
ID_DELETE_SEED_MENU = wxNewId()

# Window functions

ID_WEIGHTS_CHOICE = 10000
ID_TEAMS_LIST = 10001
ID_TEAM_DEBUG = 10002

def CreateScoreFrame( parent, call_fit = true, set_sizer = true ):
    item0 = wxBoxSizer( wxVERTICAL )
    
    item2 = wxStaticBox( parent, -1, "Weight" )
    item1 = wxStaticBoxSizer( item2, wxVERTICAL )
    
    item3 = wxChoice( parent, ID_WEIGHTS_CHOICE, wxDefaultPosition, wxSize(100,-1), [], 0 )
    item1.AddWindow( item3, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item0.AddSizer( item1, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item5 = wxStaticBox( parent, -1, "Teams" )
    item4 = wxStaticBoxSizer( item5, wxVERTICAL )
    
    item6 = wxListCtrl( parent, ID_TEAMS_LIST, wxDefaultPosition, wxSize(180,300), wxLC_REPORT|wxSUNKEN_BORDER )
    item4.AddWindow( item6, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item0.AddSizer( item4, 0, wxALIGN_CENTRE|wxALL, 5 )

    item7 = wxButton( parent, ID_TEAM_DEBUG, "Print Teams", wxDefaultPosition, wxDefaultSize, 0 )
    item0.AddWindow( item7, 0, wxALIGN_CENTRE|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

ID_TEXT = 10003
ID_START_CAPTION = 10004
ID_LINE = 10005

def WizardStartPanel( parent, call_fit = true, set_sizer = true ):
    item0 = wxBoxSizer( wxVERTICAL )
    
    item1 = wxStaticText( parent, ID_TEXT, "New Tournament", wxDefaultPosition, wxDefaultSize, 0 )
    item1.SetFont( wxFont( 16, wxSWISS, wxNORMAL, wxBOLD ) )
    item0.AddWindow( item1, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item2 = wxStaticText( parent, ID_START_CAPTION, "", wxDefaultPosition, wxDefaultSize, wxST_NO_AUTORESIZE )
    item0.AddWindow( item2, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item3 = wxStaticLine( parent, ID_LINE, wxDefaultPosition, wxSize(20,-1), wxLI_HORIZONTAL )
    item0.AddWindow( item3, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

ID_NAME_CAPTION = 10006
ID_NAME_TEXT = 10007

def WizardNamePanel( parent, call_fit = true, set_sizer = true ):
    item0 = wxBoxSizer( wxVERTICAL )
    
    item1 = wxStaticText( parent, ID_TEXT, "Name", wxDefaultPosition, wxDefaultSize, 0 )
    item1.SetFont( wxFont( 16, wxSWISS, wxNORMAL, wxBOLD ) )
    item0.AddWindow( item1, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item2 = wxStaticText( parent, ID_NAME_CAPTION, "", wxDefaultPosition, wxDefaultSize, wxST_NO_AUTORESIZE )
    item0.AddWindow( item2, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item3 = wxStaticLine( parent, ID_LINE, wxDefaultPosition, wxSize(20,-1), wxLI_HORIZONTAL )
    item0.AddWindow( item3, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item4 = wxStaticText( parent, ID_TEXT, "Tournament name", wxDefaultPosition, wxDefaultSize, 0 )
    item0.AddWindow( item4, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item5 = wxTextCtrl( parent, ID_NAME_TEXT, "", wxDefaultPosition, wxSize(200,-1), 0 )
    item0.AddWindow( item5, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

ID_TEAMS_CAPTION = 10008
ID_TEAMS_COMBO = 10009
ID_ADD_TEAM = 10010
ID_REMOVE_TEAM = 10011

def WizardTeamsPanel( parent, call_fit = true, set_sizer = true ):
    item0 = wxBoxSizer( wxVERTICAL )
    
    item1 = wxStaticText( parent, ID_TEXT, "Teams", wxDefaultPosition, wxDefaultSize, 0 )
    item1.SetFont( wxFont( 16, wxSWISS, wxNORMAL, wxBOLD ) )
    item0.AddWindow( item1, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item2 = wxStaticText( parent, ID_TEAMS_CAPTION, "", wxDefaultPosition, wxDefaultSize, wxST_NO_AUTORESIZE )
    item0.AddWindow( item2, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item3 = wxStaticLine( parent, ID_LINE, wxDefaultPosition, wxSize(20,-1), wxLI_HORIZONTAL )
    item0.AddWindow( item3, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item4 = wxBoxSizer( wxHORIZONTAL )
    
    item5 = wxComboBox( parent, ID_TEAMS_COMBO, "", wxDefaultPosition, wxSize(200,300), [], wxCB_SIMPLE )
    item4.AddWindow( item5, 0, wxGROW|wxALL, 5 )

    item6 = wxBoxSizer( wxVERTICAL )
    
    item7 = wxButton( parent, ID_ADD_TEAM, "Add", wxDefaultPosition, wxDefaultSize, 0 )
    item6.AddWindow( item7, 0, wxALIGN_CENTRE|wxALL, 5 )

    item8 = wxButton( parent, ID_REMOVE_TEAM, "Remove", wxDefaultPosition, wxDefaultSize, 0 )
    item6.AddWindow( item8, 0, wxALIGN_CENTRE|wxALL, 5 )

    item4.AddSizer( item6, 0, wxGROW|wxALIGN_CENTER_HORIZONTAL|wxALL, 5 )

    item0.AddSizer( item4, 0, wxGROW|wxALIGN_CENTER_VERTICAL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

ID_WEIGHTS_CAPTION = 10012
ID_WEIGHTS_COMBO = 10013
ID_ADD_WEIGHT = 10014
ID_REMOVE_WEIGHT = 10015
ID_ADD_STANDARD_WEIGHTS = 10016

def WizardWeightsPanel( parent, call_fit = true, set_sizer = true ):
    item0 = wxBoxSizer( wxVERTICAL )
    
    item1 = wxStaticText( parent, ID_TEXT, "Weight Classes", wxDefaultPosition, wxDefaultSize, 0 )
    item1.SetFont( wxFont( 16, wxSWISS, wxNORMAL, wxBOLD ) )
    item0.AddWindow( item1, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item2 = wxStaticText( parent, ID_WEIGHTS_CAPTION, "", wxDefaultPosition, wxDefaultSize, wxST_NO_AUTORESIZE )
    item0.AddWindow( item2, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item3 = wxStaticLine( parent, ID_LINE, wxDefaultPosition, wxSize(20,-1), wxLI_HORIZONTAL )
    item0.AddWindow( item3, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item4 = wxBoxSizer( wxHORIZONTAL )
    
    item5 = wxComboBox( parent, ID_WEIGHTS_COMBO, "", wxDefaultPosition, wxSize(200,300), [], wxCB_SIMPLE )
    item4.AddWindow( item5, 0, wxGROW|wxALL, 5 )

    item6 = wxBoxSizer( wxVERTICAL )
    
    item7 = wxButton( parent, ID_ADD_WEIGHT, "Add", wxDefaultPosition, wxDefaultSize, 0 )
    item6.AddWindow( item7, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item8 = wxButton( parent, ID_REMOVE_WEIGHT, "Remove", wxDefaultPosition, wxDefaultSize, 0 )
    item6.AddWindow( item8, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item9 = wxButton( parent, ID_ADD_STANDARD_WEIGHTS, "Add Standard", wxDefaultPosition, wxDefaultSize, 0 )
    item6.AddWindow( item9, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item4.AddSizer( item6, 0, wxGROW|wxALIGN_CENTER_HORIZONTAL|wxALL, 5 )

    item0.AddSizer( item4, 0, wxGROW|wxALIGN_CENTER_VERTICAL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

ID_LAYOUT_CAPTION = 10017
ID_LAYOUT_LIST = 10018
ID_LAYOUT_TEXT = 10019

def WizardLayoutPanel( parent, call_fit = true, set_sizer = true ):
    item0 = wxBoxSizer( wxVERTICAL )
    
    item1 = wxStaticText( parent, ID_TEXT, "Layout", wxDefaultPosition, wxDefaultSize, 0 )
    item1.SetFont( wxFont( 16, wxSWISS, wxNORMAL, wxBOLD ) )
    item0.AddWindow( item1, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item2 = wxStaticText( parent, ID_LAYOUT_CAPTION, "", wxDefaultPosition, wxDefaultSize, wxST_NO_AUTORESIZE )
    item0.AddWindow( item2, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item3 = wxStaticLine( parent, ID_LINE, wxDefaultPosition, wxSize(20,-1), wxLI_HORIZONTAL )
    item0.AddWindow( item3, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item4 = wxBoxSizer( wxHORIZONTAL )
    
    item6 = wxStaticBox( parent, -1, "Available brackets" )
    item5 = wxStaticBoxSizer( item6, wxHORIZONTAL )
    
    item7 = wxListBox( parent, ID_LAYOUT_LIST, wxDefaultPosition, wxSize(150,200), [], wxLB_SINGLE )
    item5.AddWindow( item7, 0, wxGROW|wxALL, 5 )

    item4.AddSizer( item5, 0, wxGROW|wxALIGN_CENTER_HORIZONTAL|wxALL, 5 )

    item9 = wxStaticBox( parent, -1, "Description" )
    item8 = wxStaticBoxSizer( item9, wxHORIZONTAL )
    
    item10 = wxTextCtrl( parent, ID_LAYOUT_TEXT, "", wxDefaultPosition, wxSize(250,40), wxTE_MULTILINE|wxTE_READONLY )
    item8.AddWindow( item10, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item4.AddSizer( item8, 0, wxGROW|wxALIGN_CENTER_HORIZONTAL|wxALL, 5 )

    item0.AddSizer( item4, 0, wxGROW|wxALIGN_CENTER_VERTICAL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

ID_FINISHED_CAPTION = 10020

def WizardFinishedPanel( parent, call_fit = true, set_sizer = true ):
    item0 = wxBoxSizer( wxVERTICAL )
    
    item1 = wxStaticText( parent, ID_TEXT, "Finished", wxDefaultPosition, wxDefaultSize, 0 )
    item1.SetFont( wxFont( 16, wxSWISS, wxNORMAL, wxBOLD ) )
    item0.AddWindow( item1, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item2 = wxStaticText( parent, ID_FINISHED_CAPTION, "", wxDefaultPosition, wxDefaultSize, wxST_NO_AUTORESIZE )
    item0.AddWindow( item2, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item3 = wxStaticLine( parent, ID_LINE, wxDefaultPosition, wxSize(20,-1), wxLI_HORIZONTAL )
    item0.AddWindow( item3, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

ID_WINNER_CHOICE = 10021
ID_RESULT_TYPE_RADIO = 10022
ID_RESULT_PANEL = 10023

def CreateMatchDialog( parent, call_fit = true, set_sizer = true ):
    item0 = wxBoxSizer( wxVERTICAL )
    
    item2 = wxStaticBox( parent, -1, "Winner" )
    item1 = wxStaticBoxSizer( item2, wxVERTICAL )
    
    item3 = wxChoice( parent, ID_WINNER_CHOICE, wxDefaultPosition, wxSize(150,-1), [], 0 )
    item1.AddWindow( item3, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item0.AddSizer( item1, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item4 = wxBoxSizer( wxVERTICAL )
    
    item5 = wxRadioBox( parent, ID_RESULT_TYPE_RADIO, "Win type", wxDefaultPosition, wxDefaultSize, 
        ["None","Decision","Pin","Default","Bye"] , 2, wxRA_SPECIFY_ROWS )
    item4.AddWindow( item5, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item0.AddSizer( item4, 0, wxALIGN_CENTRE|wxALL, 5 )

    item7 = wxStaticBox( parent, -1, "Result" )
    item6 = wxStaticBoxSizer( item7, wxVERTICAL )
    parent.result_sizer = item6
    
    item8 = wxPanel( parent, ID_RESULT_PANEL, wxDefaultPosition, wxSize(200,30), 0 )
    item6.AddWindow( item8, 0, wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item6, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item9 = wxBoxSizer( wxHORIZONTAL )
    
    item10 = wxButton( parent, wxID_OK, "OK", wxDefaultPosition, wxDefaultSize, 0 )
    item10.SetDefault()
    item9.AddWindow( item10, 0, wxALIGN_CENTRE|wxALL, 5 )

    item11 = wxButton( parent, wxID_CANCEL, "Cancel", wxDefaultPosition, wxDefaultSize, 0 )
    item9.AddWindow( item11, 0, wxALIGN_CENTRE|wxALL, 5 )

    item0.AddSizer( item9, 0, wxALIGN_RIGHT|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

ID_TIME_TEXT = 10024

def PinResultPanel( parent, call_fit = true, set_sizer = true ):
    item0 = wxBoxSizer( wxHORIZONTAL )
    
    item1 = wxStaticText( parent, ID_TEXT, "Time", wxDefaultPosition, wxDefaultSize, 0 )
    item0.AddWindow( item1, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item2 = wxTextCtrl( parent, ID_TIME_TEXT, "", wxDefaultPosition, wxSize(80,-1), 0 )
    item0.AddWindow( item2, 0, wxALIGN_CENTRE|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

ID_SCORE_TEXT = 10025

def DecisionResultPanel( parent, call_fit = true, set_sizer = true ):
    item0 = wxBoxSizer( wxHORIZONTAL )
    
    item1 = wxStaticText( parent, ID_TEXT, "Score", wxDefaultPosition, wxDefaultSize, 0 )
    item0.AddWindow( item1, 0, wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    item2 = wxTextCtrl( parent, ID_SCORE_TEXT, "", wxDefaultPosition, wxSize(80,-1), 0 )
    item0.AddWindow( item2, 0, wxALIGN_CENTRE|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

ID_NEW_MENU = 10026
ID_OPEN_MENU = 10027
ID_MENU = 10028
ID_SAVE_MENU = 10029
ID_SAVEAS_MENU = 10030
ID_EXIT_MENU = 10031
ID_FILE_MENU = 10032
ID_FASTFALL_MENU = 10033
ID_NUMBOUTS_MENU = 10034
ID_QUERY_MENU = 10035

def CreateMenuBar():
    item0 = wxMenuBar()
    
    item1 = wxMenu()
    item1.Append( ID_NEW_MENU, "New...\tCtrl-N", "" )
    item1.Append( ID_OPEN_MENU, "Open...\tCtrl-O", "" )
    item1.AppendSeparator()
    item1.Append( ID_SAVE_MENU, "Save\tCtrl-S", "" )
    item1.Append( ID_SAVEAS_MENU, "Save as...\tShift-Ctrl-S", "" )
    item1.AppendSeparator()
    item1.Append( ID_EXIT_MENU, "Exit", "" )
    item0.Append( item1, "File" )
    
    item2 = wxMenu()
    item2.Append( ID_FASTFALL_MENU, "Fast fall", "" )
    item2.Append( ID_NUMBOUTS_MENU, "Number of bouts", "" )
    item0.Append( item2, "Query" )
    
    return item0

# Toolbar functions


def MainToolbar( parent ):
    parent.SetMargins( [2,2] )
    
    item3 = wxChoice( parent, ID_WEIGHTS_CHOICE, wxDefaultPosition, wxSize(100,-1), [], 0 )
    parent.AddControl( item3 )
    
    parent.Realize()

# Bitmap functions


# End of generated file

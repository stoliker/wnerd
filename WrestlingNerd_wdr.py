#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: WrestlingNerd.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxWindows' modules
from wxPython.wx import *

# Window functions

ID_TEAM_LIST = 10000

def ScoreFrame( parent, call_fit = true, set_sizer = true ):
    item1 = wxStaticBox( parent, -1, "Score" )
    item0 = wxStaticBoxSizer( item1, wxVERTICAL )
    
    item2 = wxListCtrl( parent, ID_TEAM_LIST, wxDefaultPosition, wxSize(180,300), wxLC_REPORT|wxSUNKEN_BORDER )
    item0.AddWindow( item2, 0, wxGROW|wxALIGN_CENTER_VERTICAL|wxALL, 5 )

    if set_sizer == true:
        parent.SetAutoLayout( true )
        parent.SetSizer( item0 )
        if call_fit == true:
            item0.Fit( parent )
            item0.SetSizeHints( parent )
    
    return item0

ID_TEXT = 10001
ID_START_CAPTION = 10002
ID_LINE = 10003

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

ID_NAME_CAPTION = 10004
ID_NAME_TEXT = 10005

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

ID_TEAMS_CAPTION = 10006
ID_TEAMS_COMBO = 10007
ID_ADD_TEAM = 10008
ID_REMOVE_TEAM = 10009

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

ID_WEIGHTS_CAPTION = 10010
ID_WEIGHTS_COMBO = 10011
ID_ADD_WEIGHT = 10012
ID_REMOVE_WEIGHT = 10013
ID_ADD_STANDARD_WEIGHTS = 10014

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

ID_LAYOUT_CAPTION = 10015
ID_LAYOUT_LIST = 10016
ID_LAYOUT_TEXT = 10017

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
    item10.Enable(false)
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

ID_FINISHED_CAPTION = 10018

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

# Menubar functions

ID_NEW_MENU = 10019
ID_OPEN_MENU = 10020
ID_MENU = 10021
ID_SAVE_MENU = 10022
ID_SAVEAS_MENU = 10023
ID_EXIT_MENU = 10024
ID_FILE_MENU = 10025
ID_FASTFALL_MENU = 10026
ID_NUMBOUTS_MENU = 10027
ID_QUERY_MENU = 10028

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

ID_WEIGHT_CLASSES = 10029

def CreateToolbar( parent ):
    parent.SetMargins( [2,2] )
    
    item3 = wxChoice( parent, ID_WEIGHT_CLASSES, wxDefaultPosition, wxSize(100,-1), [], 0 )
    parent.AddControl( item3 )
    
    parent.Realize()

# Bitmap functions


# End of generated file

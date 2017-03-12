library(shinydashboard)
library(shiny)

dashboardPage(

  dashboardHeader(title = "Max Hit Users"),
  dashboardSidebar(
    h3("AppZap"),
    hr(),
       sidebarMenu(
      menuItem("Top Users",tabName = "barchart",icon = icon("bar-chart"))
      #menuItem("Map",tabName = "map",icon = icon("smile-o"))
    )
  ),

  dashboardBody(

      tabItem(tabName = "barchart",

              fluidRow(

                tabBox(title = "",width = 12,

                       tabPanel(title = tagList(shiny::icon("heart"),"Top Users"),

                                plotOutput("bar1")
                       )


                )


              )


      )
  )
  )



﻿using Sahaara.Style;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace Sahaara
{
    // Learn more about making custom code visible in the Xamarin.Forms previewer
    // by visiting https://aka.ms/xamarinforms-previewer
    [DesignTimeVisible(false)]
    public partial class MainPage : ContentPage
    {
        
        public MainPage()
        {
            InitializeComponent();
        }

        protected override void OnAppearing()
        {
            base.OnAppearing(); 
            DependencyService.Get<IStatusBarStyleManager>().SetDarkTheme();
        }
        private async void LoginButton_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new HomePage());
        }

        private async void TapGestureRecognizer_Tapped(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new SignupPage());
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;

namespace Sahaara.Droid
{
    [Activity(Label = "Sahaara" , NoHistory = true, MainLauncher = true, Icon = "@mipmap/icon", Theme = "@style/MyTheme.Splash")]
    public class SplashActivity : Activity
    {
        protected override void OnCreate(Bundle savedInstanceState)
        {
            base.OnCreate(savedInstanceState);
            Intent intent = new Intent(this, typeof(MainActivity));
            StartActivity(intent);
            // Create your application here
        }
    }
}
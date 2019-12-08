using Sahaara.Style;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace Sahaara
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class HomePage : ContentPage
    {
        public HomePage()
        {
            InitializeComponent();
        }

        protected override void OnAppearing()
        {
            base.OnAppearing();
            DependencyService.Get<IStatusBarStyleManager>().SetLightTheme();
        }

        private async void SwipeGestureRecognizer_Swiped(object sender, SwipedEventArgs e)
        {
            await Navigation.PushModalAsync(new PublicFeed(), true);
        }

        private async void ImageButton_Clicked(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new PublicFeed(), true);
        }

        private async void ImageButton_Clicked_1(object sender, EventArgs e)
        {
            await Navigation.PushModalAsync(new MapPage(), true);
        }
    }
}
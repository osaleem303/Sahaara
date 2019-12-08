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
    public partial class PublicFeed : ContentPage
    {
        public PublicFeed()
        {
            InitializeComponent();
            DependencyService.Get<IStatusBarStyleManager>().SetDarkTheme();
        }
    }
}